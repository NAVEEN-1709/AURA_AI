"""
AURA AI

Ollama LLM Provider

Connects AURA to locally running Ollama models.
"""

from ollama import AsyncClient

from core.logger import logger
from llm.models import ChatMessage, ChatResponse
from llm.providers.base import BaseLLMProvider


class OllamaProvider(BaseLLMProvider):
    """
    LLM provider for local Ollama models.
    """

    def __init__(
        self,
        model: str = "llama3.2:3b",
        host: str = "http://localhost:11434",
    ) -> None:
        self._model = model
        self._client = AsyncClient(host=host)

        logger.info(
            "Ollama provider initialized with model '{}'",
            self._model,
        )

    @property
    def name(self) -> str:
        return "ollama"

    async def generate(
        self,
        messages: list[ChatMessage],
        model: str | None = None,
    ) -> ChatResponse:
        """
        Generate a response using Ollama.
        """

        selected_model = model or self._model

        ollama_messages = [
            {
                "role": message.role.value,
                "content": message.content,
            }
            for message in messages
        ]

        logger.info(
            "Sending request to Ollama using model '{}'",
            selected_model,
        )

        try:
            response = await self._client.chat(
                model=selected_model,
                messages=ollama_messages,
            )

            content = response["message"]["content"]

            logger.success(
                "Ollama response received successfully."
            )

            return ChatResponse(
                content=content,
                provider=self.name,
                model=selected_model,
            )

        except Exception:
            logger.exception(
                "Ollama request failed."
            )
            raise