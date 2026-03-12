from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.orchestrator import graph


app = FastAPI(
    title="Java RAG Code Generator",
    description="Multi-Agent RAG system for Java code generation",
    version="1.0"
)


class QueryRequest(BaseModel):

    query: str


class CodeResponse(BaseModel):

    code: str
    valid: bool


@app.post("/generate", response_model=CodeResponse)
def generate_code(request: QueryRequest):

    result = graph.invoke({

        "query": request.query

    })

    return {

        "code": result.get("generated_code", ""),
        "valid": result.get("valid", False)

    }