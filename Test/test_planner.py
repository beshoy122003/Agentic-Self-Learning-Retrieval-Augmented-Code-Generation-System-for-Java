from app.agents.planner_agent import planner_agent


state = {

"query": "Write a Java function to reverse a string"

}

result = planner_agent(state)

print(result["plan"])