from app.retrieval.embedder import Embedder
from app.retrieval.vectordb import VectorDB
from data.load_dataset import load_java_codegen_dataset

print("Starting indexing pipeline...")

embedder = Embedder()
db = VectorDB()

dataset = load_java_codegen_dataset(limit=5000)

prompts = [item["prompt"] for item in dataset]
codes = [item["code"] for item in dataset]
ids = [item["id"] for item in dataset]

print("Generating embeddings...")

embeddings = embedder.model.encode(
    prompts,
    batch_size=128,
    show_progress_bar=True
)

print("Saving to vector DB...")

metadatas = [{"code": code} for code in codes]

db.collection.add(
    ids=ids,
    documents=prompts,
    embeddings=[e.tolist() for e in embeddings],
    metadatas=metadatas
)

print("Index built successfully")