"""
AURA AI

Base LLM Provider
"""

from abc import ABC, abstractmethod

from llm.models import ChatMessage, ChatResponse


class BaseLLMProvider(ABC):
    """
    Abstract interface implemented by every LLM provider.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the provider name."""

    @abstractmethod
    async def generate(
        self,
        messages: list[ChatMessage],
        model: str | None = None,
    ) -> ChatResponse:
        """
        Generate a response from the language model.
        """

        raise NotImplementedError