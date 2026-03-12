from app.llm.model_loader import get_llm

model, tokenizer = get_llm()


def planner_agent(state):

    query = state["query"]

    prompt = f"""
You are a planning agent in a multi-agent coding system.

Break the task into clear steps.

User request:
{query}

Return a short numbered plan.
"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    outputs = model.generate(
        **inputs,
        max_new_tokens=120
    )

    plan = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return {
        "plan": plan
    }