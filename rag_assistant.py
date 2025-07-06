import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.storage.storage_context import StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import chromadb

# Load .env
load_dotenv()
DATA_PATH = os.getenv("DATA_PATH", "./docs")

# Configure embedding model
embedding_model = HuggingFaceEmbedding(model_name="all-MiniLM-L6-v2")

# Load documents
print(f"Loading documents from: {DATA_PATH}")
documents = SimpleDirectoryReader(DATA_PATH).load_data()

# Chunk documents
print("Chunking documents...")
parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
nodes = parser.get_nodes_from_documents(documents)

# Setup Chroma
print("Setting up ChromaDB...")
chroma_client = chromadb.PersistentClient(path="./chroma")
collection = chroma_client.get_or_create_collection("noc_docs")
vector_store = ChromaVectorStore(chroma_collection=collection)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(nodes, storage_context=storage_context)

# Query loop
query_engine = index.as_query_engine()
print("Ready to query.")

while True:
    q = input("\nAsk NOCLLAMA a question (or type 'exit'): ")
    if q.strip().lower() in ("exit", "quit"):
        break
    print("\n" + str(query_engine.query(q)))