"""
AURA AI

Chat Session

Maintains the conversation history for a single
active conversation.
"""

from llm.models import ChatMessage, ChatRole


class ChatSession:
    """
    Maintains short-term conversation history.
    """

    def __init__(
        self,
        system_prompt: str,
        max_messages: int = 20,
    ) -> None:
        self._system_prompt = system_prompt
        self._max_messages = max_messages

        self._messages: list[ChatMessage] = []

    @property
    def messages(self) -> list[ChatMessage]:
        """
        Return the current conversation messages.

        A copy is returned so callers cannot directly
        modify the internal session state.
        """

        return list(self._messages)

    def add_user_message(
        self,
        content: str,
    ) -> None:
        """Add a user message."""

        self._messages.append(
            ChatMessage(
                role=ChatRole.USER,
                content=content,
            )
        )

        self._trim_history()

    def add_assistant_message(
        self,
        content: str,
    ) -> None:
        """Add an assistant response."""

        self._messages.append(
            ChatMessage(
                role=ChatRole.ASSISTANT,
                content=content,
            )
        )

        self._trim_history()

    def get_messages(self) -> list[ChatMessage]:
        """
        Return the complete message list including
        the system prompt.
        """

        return [
            ChatMessage(
                role=ChatRole.SYSTEM,
                content=self._system_prompt,
            ),
            *self._messages,
        ]

    def clear(self) -> None:
        """Clear the current conversation."""

        self._messages.clear()

    def _trim_history(self) -> None:
        """
        Keep only the most recent messages.

        This prevents the conversation from growing
        indefinitely.
        """

        if len(self._messages) > self._max_messages:
            self._messages = self._messages[
                -self._max_messages:
            ]