"""
Base interface for all LLM providers.
"""

from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    """
    Abstract interface for language model providers.
    """

    @abstractmethod
    async def generate_response(
        self,
        message: str,
    ) -> str:
        """
        Generate a response from the model.
        """
        raise NotImplementedError