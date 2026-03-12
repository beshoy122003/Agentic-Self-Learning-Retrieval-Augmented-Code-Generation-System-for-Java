import chromadb


class VectorDB:

    def __init__(self):

        print("Starting ChromaDB")

        self.client = chromadb.PersistentClient(
            path="./vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="java_code"
        )

    def add(self, doc_id, prompt, embedding, code):

        self.collection.add(
            ids=[doc_id],
            documents=[prompt],
            embeddings=[embedding],
            metadatas=[{"code": code}]
        )

    def search(self, embedding, k=3):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )

        return results