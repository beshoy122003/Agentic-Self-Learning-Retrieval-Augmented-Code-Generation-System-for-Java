from app.retrieval.embedder import get_embedder
from app.retrieval.vectordb import VectorDB
import uuid

embedder = get_embedder()
vectordb = VectorDB()


def learn_new_example(query, code):

    embedding = embedder.encode(query).tolist()

    vectordb.collection.add(
        ids=[str(uuid.uuid4())],
        documents=[query],
        embeddings=[embedding],
        metadatas=[{"code": code}]
    )

    print("New knowledge added to vector DB")