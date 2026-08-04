import asyncio

from agents.conversation_agent import ConversationAgent


async def main():
    agent = ConversationAgent()

    await agent.initialize()
    await agent.start()

    response = await agent.process_message(
        "Hello Aura"
    )

    print()
    print("Response:")
    print(response)

    await agent.stop()
    await agent.shutdown()


if __name__ == "__main__":
    asyncio.run(main())