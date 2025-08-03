from pydantic import BaseModel
from langchain.memory import ConversationBufferMemory
from langchain.schema import BaseChatMessageHistory

from app.web.api import (
    get_messages_by_conversation_id,
    add_message_to_conversation,
)


class SQLMessageHistory(BaseChatMessageHistory, BaseModel):
    conversation_id: str

    @property
    def messages(self):
        """
        Fetch messages from the database for the given conversation_id.
        """
        return get_messages_by_conversation_id(self.conversation_id)

    def add_message(self, message):
        """
        Add a message to the conversation in the database.
        """
        add_message_to_conversation(
            conversation_id=self.conversation_id,
            role=message.type,
            content=message.content,
        )

    def clear(self):
        pass


def build_memory(chat_args):
    """
    Build a memory object for the chat.

    :param chat_args: ChatArgs object containing conversation_id.
    :return: A ConversationBufferMemory object.
    """
    return ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",
        chat_memory=SQLMessageHistory(conversation_id=chat_args.conversation_id),
        return_messages=True,
    )
