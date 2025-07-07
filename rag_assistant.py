import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
import chromadb

load_dotenv()
DATA_PATH = os.getenv("DATA_PATH", "./docs")

embedding_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")
Settings.embed_model = embedding_model

# Optional: use Ollama as LLM if enabled
if os.getenv("USE_OLLAMA", "false").lower() == "true":
    from llama_index.llms.ollama import Ollama
    ollama_model = os.getenv("OLLAMA_MODEL", "mistral")
    print(f"Using local LLM via Ollama: {ollama_model}")
    Settings.llm = Ollama(model=ollama_model)

# Load documents
print(f"Loading documents from: {DATA_PATH}")
documents = SimpleDirectoryReader(DATA_PATH).load_data()
print(f"Loaded {len(documents)} document(s)")

# Chunk documents
print("Chunking documents...")
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)

# Setup Chroma
print("Setting up ChromaDB vector store...")
chroma_client = chromadb.PersistentClient(path="./chroma")
collection = chroma_client.get_or_create_collection("noc_docs")
vector_store = ChromaVectorStore(chroma_collection=collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)

# Query loop
query_engine = index.as_query_engine()
print("NOCLLAMA is ready. Ask it a question (or type 'exit').\n")
while True:
    query = input("❓> ").strip()
    if query.lower() in {"exit", "quit"}:
        print("Exiting NOCLLAMA.")
        break
    response = query_engine.query(query)
    print(f"\n{response}\n")