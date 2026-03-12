from app.llm.model_loader import get_llm
from app.tools.memory_tool import memory

from app.utils.code_cleaner import extract_java_code

model, tokenizer = get_llm()


def writer_agent(state):

    query = state["query"]
    plan = state["plan"]
    context = state["context"]

    history = memory.get_context()

    examples = "\n\n".join(context[:2])

    prompt = f"""
You are an expert Java developer.

Your task is to write Java code.

User request:
{query}

Plan:
{plan}

Here are similar Java examples:
{examples}

Rules:
- Return ONLY Java code
- Do not explain
- Do not repeat the plan
- Do not add text

Java Code:
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        temperature=0.2
    )

    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

    code = extract_java_code(result)

    return {
        "generated_code": code
    }