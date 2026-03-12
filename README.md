# Agentic Self-Learning Retrieval-Augmented Code Generation System for Java

An advanced **Agentic RAG system** that generates **compilable Java code** using a multi-agent architecture powered by **LangGraph, FastAPI, ChromaDB, and LLMs**.

Unlike traditional code generation systems that rely solely on LLMs, this system **retrieves relevant code examples, generates code, validates it using the Java compiler, and continuously improves by learning from successful generations.**

---

# Key Idea

Traditional LLM code generation often suffers from:

- hallucinated code
- syntactic errors
- lack of grounding
- no runtime validation

This project solves those issues using **Agentic Retrieval-Augmented Generation (RAG)** with an execution feedback loop.

The system:

1. Retrieves relevant code examples
2. Plans the solution
3. Generates Java code
4. Compiles the code
5. Learns from successful outputs

---

# System Architecture

```
User Query
│
▼
Planner Agent
│
▼
Researcher Agent (RAG Retrieval)
│
▼
Writer Agent (LLM Code Generation)
│
▼
Critic Agent (Java Compiler Validation)
│
├── Success → Continual Learning
│
└── Failure → Regeneration Loop
│
▼
FastAPI API
```

---

# Multi-Agent Pipeline

The system uses **LangGraph orchestration** to coordinate multiple agents.

### Planner Agent

Breaks down the user's request into reasoning steps.

Example:

```
write java function to check palindrome
```

Plan generated:

```
1. Define a function
2. Normalize string
3. Compare characters from both ends
4. Return boolean result
```

---

### Researcher Agent

Performs **semantic retrieval** using embeddings.

- Embedding model: `SentenceTransformers`
- Vector database: `ChromaDB`

This retrieves **similar Java implementations** to ground the LLM.

---

### Writer Agent

Generates Java code using a language model.

Inputs:

- user query
- reasoning plan
- retrieved examples
- conversation memory

Output:

```
valid Java code
```

---

### Critic Agent

Validates generated code using **actual Java compilation**.

```
javac Generated.java
```

If compilation fails:

```
Writer Agent is triggered again
```

This creates a **self-correcting generation loop**.

---

# Retrieval System (RAG)

The retrieval system stores Java examples in a vector database.

Dataset entry format:

```python
{
 "id": sample_id,
 "prompt": natural_language_description,
 "code": java_function
}
```

Each prompt is embedded:

```
E(prompt) → vector
```

Similarity search uses **cosine similarity**:

```
sim(q,p) = (v_q ⋅ v_p) / (||v_q|| ||v_p||)
```

The top-k examples are injected into the prompt.

---

# Memory System

The system includes **conversation memory**.

Recent interactions are stored and passed to the LLM to improve responses.

Example memory:

```
User: reverse string
Assistant: Java code

User: check palindrome
Assistant: Java code
```

---

# Continual Learning

If a generated program successfully compiles, it is stored back into the vector database.

```
D_{t+1} = D_t ∪ {(query, generated_code)}
```

This allows the system to **improve retrieval over time**.

---

# Technology Stack

| Component         | Technology               |
| ----------------- | ------------------------ |
| LLM Orchestration | LangGraph                |
| API               | FastAPI                  |
| Vector Database   | ChromaDB                 |
| Embeddings        | SentenceTransformers     |
| Code Generation   | HuggingFace Transformers |
| Validation        | Java Compiler (`javac`)  |
| Deployment        | Docker + CUDA            |

---

# Project Structure

```
app/
│
├── agents/
│   ├── planner_agent.py
│   ├── researcher_agent.py
│   ├── writer_agent.py
│   └── critic_agent.py
│
├── retrieval/
│   ├── embedder.py
│   ├── retriever.py
│   └── vectordb.py
│
├── execution/
│   └── java_executor.py
│
├── tools/
│   ├── memory_tool.py
│   └── learning_tool.py
│
├── graph/
│   └── orchestrator.py
│
├── api/
│   └── main.py
│
└── utils/
    └── code_cleaner.py
```

---

# Installation

Clone the repository:

```
git clone https://github.com/beshoy122003/Agentic-Self-Learning-Retrieval-Augmented-Code-Generation-System-for-Java.git
```

```
cd Agentic-Self-Learning-Retrieval-Augmented-Code-Generation-System-for-Java
```

Create environment:

```
conda create -n rag_code python=3.10
```

```
conda activate rag_code
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Build Retrieval Index

Before running the system, build the vector index:

```
python run.py
```

This step:

- embeds dataset prompts
- stores vectors in ChromaDB

---

# Run API Server

```
uvicorn app.api.main:app --reload
```

Open API docs:

```
http://localhost:8000/docs
```

---

# Example API Request

POST `/generate`

```
{
 "query": "write java function to check palindrome"
}
```

Response:

```
{
 "code": "public class Main { ... }",
 "valid": true
}
```

---

# Docker Deployment

Build image:

```
docker build -t java-rag .
```

Run container:

```
docker run --gpus all -p 8000:8000 java-rag
```

---

# Evaluation Metrics

### Compilation Success Rate

```
CSR = successful_compilations / total_generations
```

### Retrieval Quality

Average cosine similarity between query and retrieved prompts.

### Latency

```
T_total = T_retrieve + T_generate + T_validate
```

---

# Challenges

- Limited GPU memory
- LLM output cleaning
- Java compilation sandboxing
- prompt engineering

---

# Future Work

- cross-encoder reranking
- AST-aware code retrieval
- automatic test generation
- multi-language code generation