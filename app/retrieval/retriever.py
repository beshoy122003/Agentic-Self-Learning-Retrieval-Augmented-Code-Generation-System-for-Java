from app.retrieval.embedder import get_embedder
from app.retrieval.vectordb import VectorDB


_embedder = None
_db = None


def get_retriever():

    global _embedder, _db

    if _embedder is None:
        _embedder = get_embedder()

    if _db is None:
        _db = VectorDB()

    return _embedder, _db


def retrieve(query):

    embedder, db = get_retriever()

    embedding = embedder.encode(query).tolist()

    results = db.search(embedding)

    docs = results["documents"][0]
    codes = [m["code"] for m in results["metadatas"][0]]

    return docs, codes, embedding