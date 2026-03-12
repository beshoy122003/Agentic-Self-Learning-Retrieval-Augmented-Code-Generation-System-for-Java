from app.graph.orchestrator import graph


query = "write java function to check palindrome"

result = graph.invoke({

"query":query

})

print("\nGenerated Code:\n")

print(result["generated_code"])