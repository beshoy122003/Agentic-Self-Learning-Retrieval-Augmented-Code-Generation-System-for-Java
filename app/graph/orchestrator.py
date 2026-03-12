from typing import TypedDict
from langgraph.graph import StateGraph, END

from app.agents.planner_agent import planner_agent
from app.agents.researcher_agent import researcher_agent
from app.agents.writer_agent import writer_agent
from app.agents.critic_agent import critic_agent


class AgentState(TypedDict):

    query: str
    plan: str
    context: list
    generated_code: str
    valid: bool
    attempts: int


# إنشاء الجراف
builder = StateGraph(AgentState)

# إضافة الـ nodes
builder.add_node("planner", planner_agent)
builder.add_node("researcher", researcher_agent)
builder.add_node("writer", writer_agent)
builder.add_node("critic", critic_agent)

# نقطة البداية
builder.set_entry_point("planner")

# المسار الأساسي
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "writer")
builder.add_edge("writer", "critic")


# Routing بعد الـ critic
def route_after_critic(state):

    # إذا الكود صحيح → إنهاء
    if state["valid"]:
        return END

    # إذا وصلنا 3 محاولات → إنهاء
    if state["attempts"] >= 3:
        return END

    # غير ذلك → إعادة الكتابة
    return "writer"


# إضافة الـ conditional edge
builder.add_conditional_edges(
    "critic",
    route_after_critic
)

# compile graph
graph = builder.compile()