from app.retrieval.retriever import retrieve


def researcher_agent(state):

    query = state["query"]

    docs, codes, embedding = retrieve(query)

    return {

        "context": codes,
        "embedding": embedding

    }