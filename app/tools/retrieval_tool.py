from ..retrieval.retriever import Retriever


retriever = Retriever()


def retrieve_code_examples(query):

    docs, codes, embedding = retriever.retrieve(query)

    return {
        "docs": docs,
        "codes": codes,
        "embedding": embedding
    }