from app.llm.model_loader import LLMModel


llm = LLMModel()

prompt = "Write a Java function to reverse a string"

result = llm.generate(prompt)

print(result)