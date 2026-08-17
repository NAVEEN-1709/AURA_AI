"""
AURA AI

LLM Router

Routes requests to the configured language model provider.
"""

from llm.models import ChatMessage, ChatResponse
from llm.providers.base import BaseLLMProvider
from core.logger import logger


class LLMRouter:
    """
    Routes LLM requests to the appropriate provider.
    """

    def __init__(
        self,
        providers: dict[str, BaseLLMProvider],
        default_provider: str,
    ) -> None:
        if not providers:
            raise ValueError("At least one LLM provider is required.")

        if default_provider not in providers:
            raise ValueError(
                f"Default provider '{default_provider}' "
                f"is not registered."
            )

        self._providers = providers
        self._default_provider = default_provider

        logger.info(
            "LLM Router initialized. Default provider: '{}'",
            default_provider,
        )

    def get_provider(
        self,
        provider_name: str | None = None,
    ) -> BaseLLMProvider:
        """
        Return the requested provider or the default provider.
        """

        name = provider_name or self._default_provider

        try:
            return self._providers[name]
        except KeyError as exc:
            raise ValueError(
                f"LLM provider '{name}' is not registered."
            ) from exc

    async def generate(
        self,
        messages: list[ChatMessage],
        provider: str | None = None,
        model: str | None = None,
    ) -> ChatResponse:
        """
        Generate a response through the selected provider.
        """

        selected_provider = self.get_provider(provider)

        logger.info(
            "Routing request to provider '{}'",
            selected_provider.name,
        )

        return await selected_provider.generate(
            messages=messages,
            model=model,
        )

    def list_providers(self) -> list[str]:
        """
        Return all available provider names.
        """

        return list(self._providers.keys())

    @property
    def default_provider(self) -> str:
        """Return the default provider name."""

        return self._default_provider