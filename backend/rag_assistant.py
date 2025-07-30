from pathlib import Path
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, ServiceContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.storage.docstore import SimpleDocumentStore
from llama_index.core.storage.storage_context import StorageContext
from chromadb import PersistentClient
from llama_index.core.settings import Settings
from fastapi import FastAPI, UploadFile, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from llama_index.core.query_engine import RetrieverQueryEngine
from starlette.responses import StreamingResponse
import os, logging

logging.basicConfig(filename="query.log", level=logging.INFO)

# === Configuration ===
DOCS_DIR = "./docs"
CHROMA_DIR = "./chroma_store"

print("Using local LLM via Ollama: mistral")

# Load documents
print(f"Loading documents from: {DOCS_DIR}")
documents = SimpleDirectoryReader(DOCS_DIR).load_data()
print(f"Loaded {len(documents)} document(s)")

# Chunking
print("Chunking documents...")
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)

# Vector store
print("Setting up ChromaDB vector store...")
client = PersistentClient(path=CHROMA_DIR)
chroma_collection = client.get_or_create_collection("rag-index")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

# Storage context
storage_context = StorageContext.from_defaults(
    docstore=SimpleDocumentStore(),
    vector_store=vector_store,
    index_store=SimpleIndexStore(),
)

# LLM & ServiceContext
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
llm = Ollama(model="mistral", request_timeout=120)

Settings.llm = llm
Settings.embed_model = embed_model

# Build index and query engine
index = VectorStoreIndex(nodes, storage_context=storage_context)
query_engine = RetrieverQueryEngine.from_args(
    retriever=index.as_retriever(),
    llm=llm
)

def get_query_engine():
    return query_engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

# CLI interface
if __name__ == "__main__":
    print("NOCLLAMA is ready. Ask it a question (or type 'exit').\n")
    while True:
        user_input = input("❓> ")
        if user_input.lower() in ("exit", "quit"):
            break
        response = query_engine.query(user_input)
        print(f"\n🤖 {response}\n")

api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

@app.post("/query")
def query_route(request: QueryRequest, api_key: str = Depends(api_key_header)):
    # Optional API key check
    expected_key = os.getenv("API_KEY")
    if expected_key and api_key != expected_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    prompt = f"Respond in Markdown format.\n\n{request.question}"
    response = query_engine.query(prompt)
    sources = [
        {"text": node.node.text, "score": node.score, "source": node.node.metadata.get("file_name", "")}
        for node in response.source_nodes
    ]
    return {"answer": str(response), "sources": sources}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "model": "mistral",
        "embedding_model": "BAAI/bge-small-en-v1.5",
        "docs_loaded": len(documents),
        "chunks": len(nodes)
    }

@app.post("/upload")
async def upload_file(file: UploadFile):
    contents = await file.read()
    save_path = Path(DOCS_DIR) / file.filename
    with open(save_path, "wb") as f:
        f.write(contents)
    return {"status": "uploaded", "filename": file.filename}

def stream_query_response(question: str):
    prompt = f"Respond in Markdown format.\n\n{question}"
    response = query_engine.query(prompt, stream=True)

    async def event_generator():
        for token in response.response_gen:
            yield f"data: {token}\n\n"

    return response  # This will be a StreamingResponse or similar

@app.post("/query-stream")
async def stream_query(data: dict):
    question = data.get("question")
    response = stream_query_response(question)

    async def event_generator():
        for token in response.response_gen:
            yield f"data: {token}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")