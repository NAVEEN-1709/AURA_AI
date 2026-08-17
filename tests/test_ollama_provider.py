"""
Test Ollama provider.
"""

import asyncio

from llm.models import ChatMessage, ChatRole
from llm.providers.ollama_provider import OllamaProvider


async def main() -> None:
    provider = OllamaProvider(
        model="llama3.2:3b"
    )

    messages = [
        ChatMessage(
            role=ChatRole.SYSTEM,
            content="You are AURA, a helpful personal AI assistant.",
        ),
        ChatMessage(
            role=ChatRole.USER,
            content="Hello Aura. Introduce yourself briefly.",
        ),
    ]

    response = await provider.generate(messages)

    print()
    print("=" * 60)
    print("AURA RESPONSE")
    print("=" * 60)
    print(response.content)
    print()
    print(f"Provider: {response.provider}")
    print(f"Model: {response.model}")


if __name__ == "__main__":
    asyncio.run(main())