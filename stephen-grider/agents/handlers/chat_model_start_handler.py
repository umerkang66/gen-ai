from langchain.callbacks.base import BaseCallbackHandler
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))


class ChatModelStartHandler(BaseCallbackHandler):
    """Callback handler to handle the start of a chat model invocation."""

    def on_chat_model_start(self, serialized: dict, messages, **kwargs: dict) -> None:
        """Handle the start of a chat model invocation."""

        print("\n\n\n\n========== Sending Messages ==========\n\n")
        for message in messages[0]:
            if message.type == "system":
                boxen_print(
                    message.content,
                    title=message.type,
                    color="yellow",
                )

            elif message.type == "human":
                boxen_print(
                    message.content,
                    title=message.type,
                    color="green",
                )

            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                call = message.additional_kwargs["function_call"]
                boxen_print(
                    f"Running tool {call['name']} with args {call['arguments']}",
                    title=message.type,
                    color="cyan",
                )

            elif message.type == "ai":
                boxen_print(
                    message.content,
                    title=message.type,
                    color="blue",
                )

            elif message.type == "function":
                boxen_print(
                    message.content,
                    title=message.type,
                    color="purple",
                )

            else:
                boxen_print(
                    message.content,
                    title=message.type,
                )
