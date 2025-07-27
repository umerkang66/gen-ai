import argparse
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain.chains.sequential import SequentialChain
from langchain.chains import LLMChain


parser = argparse.ArgumentParser()
parser.add_argument("--language", type=str, default="python")
parser.add_argument("--tasks", type=str, default="return a list of numbers")
args = parser.parse_args()


llm = OllamaLLM(model="llama3.2:latest")


code_prompt = PromptTemplate.from_template(
    "Write a {language} code snippet that will {tasks}."
)
test_prompt = PromptTemplate.from_template(
    "Write a {language} test code that will test the following code:\n\n{code}\n"
)


code_chain = LLMChain(prompt=code_prompt, llm=llm, output_key="code")
test_chain = LLMChain(prompt=test_prompt, llm=llm, output_key="test")

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=["language", "tasks"],
    output_variables=["code", "test"],
)

result = chain.invoke({"language": args.language, "tasks": args.tasks})

print(">>>>>>>>> GENERATED CODE:")
print(result["code"])

print(">>>>>>>>> GENERATED TEST:")
print(result["test"])
