from sentence_transformers import SentenceTransformer

_embedder = None


def get_embedder():

    global _embedder

    if _embedder is None:

        print("Loading embedding model")

        _embedder = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    return _embedder