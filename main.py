from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2:latest")


response = llm.invoke("Create a very very simple poem")
print(response)
