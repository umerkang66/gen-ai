from langchain.vectorstores.chroma import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_ollama import OllamaEmbeddings, ChatOllama

chat = ChatOllama(model="llama3.2:latest")
embeddings = OllamaEmbeddings(model="llama3.2:latest")


db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings,
)

retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff",
)

result = chain.run("What is an interesting fact about the English language?")

print(result)
