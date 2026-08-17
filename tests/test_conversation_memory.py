"""
Test AURA conversation memory.
"""

import asyncio

from agents.conversation_agent import ConversationAgent
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

    agent = ConversationAgent(
        llm_router=router,
    )

    await agent.initialize()
    await agent.start()

    response = await agent.process_message(
        "My name is Naveen."
    )

    print()
    print("AURA >", response)

    response = await agent.process_message(
        "What is my name?"
    )

    print()
    print("AURA >", response)

    await agent.stop()
    await agent.shutdown()


if __name__ == "__main__":
    asyncio.run(main())