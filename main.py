from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--language", type=str, default="python")
parser.add_argument("--tasks", type=str, default="return a list of numbers")
args = parser.parse_args()


llm = OllamaLLM(model="llama3.2:latest")

code_prompt = PromptTemplate.from_template(
    "Write a {language} code snippet that will {tasks}."
)

code_chain = code_prompt | llm

result = code_chain.invoke(
    {
        "language": args.language, 
        "tasks": args.tasks
    }
)

print(result)
