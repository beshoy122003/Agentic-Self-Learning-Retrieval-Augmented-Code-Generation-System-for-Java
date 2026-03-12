from app.agents.researcher_agent import researcher_agent


state = {

"query": "sort an array"

}

result = researcher_agent(state)

print("\nRetrieved Code Examples:\n")

for code in result["context"]:

    print(code)
    print("------")