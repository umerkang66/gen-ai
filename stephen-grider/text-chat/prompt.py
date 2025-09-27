from langchain.vectorstores.chroma import Chroma
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_ollama import OllamaEmbeddings, ChatOllama
from redundant_filter_retriever import RedundantFilterRetriever


chat = ChatOllama(model="llama3.2:latest")
embeddings = OllamaEmbeddings(model="llama3.2:latest")


db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings,
)

# if we don't have the redundant data, use this
# retriever = db.as_retriever()
retriever = RedundantFilterRetriever(
    embeddings=embeddings,
    chroma=db,
)

chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=retriever,
    chain_type="stuff",
)

result = chain.run("which food is made without destroying any kind of life?")

print(result)
