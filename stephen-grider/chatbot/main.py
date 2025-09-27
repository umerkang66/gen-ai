from langchain_ollama import ChatOllama
from langchain.prompts import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
from langchain.chains import LLMChain


chat = ChatOllama(model="llama3.2:latest")


memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
)


prompt = ChatPromptTemplate(
    input_variables=["content", "messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)


chain = LLMChain(llm=chat, prompt=prompt, memory=memory)


while True:
    content = input(">> ")
    result = chain.invoke({"content": content})
    print(result["text"])
