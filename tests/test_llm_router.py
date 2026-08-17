"""
Test LLM Router.
"""

import asyncio

from llm.models import ChatMessage, ChatRole
from llm.providers.ollama_provider import OllamaProvider
from llm.router import LLMRouter


async def main() -> None:
    ollama = OllamaProvider(
        model="llama3.2:3b"
    )

    router = LLMRouter(
        providers={
            "ollama": ollama,
        },
        default_provider="ollama",
    )

    print()
    print("Available providers:")
    print(router.list_providers())

    messages = [
        ChatMessage(
            role=ChatRole.SYSTEM,
            content=(
                "You are AURA, a concise and friendly "
                "personal AI assistant."
            ),
        ),
        ChatMessage(
            role=ChatRole.USER,
            content="What is the purpose of AURA AI?",
        ),
    ]

    response = await router.generate(
        messages=messages,
    )

    print()
    print("=" * 60)
    print("AURA")
    print("=" * 60)
    print(response.content)
    print()
    print(f"Provider: {response.provider}")
    print(f"Model: {response.model}")


if __name__ == "__main__":
    asyncio.run(main())