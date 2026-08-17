"""
Test Memory Agent.
"""

import asyncio

from memory.agent import MemoryAgent
from memory.database import MemoryDatabase
from memory.manager import MemoryManager


async def main() -> None:

    database = MemoryDatabase(
        database_path="database/test_agent_memory.db"
    )

    manager = MemoryManager(
        database=database
    )

    agent = MemoryAgent(
        memory_manager=manager
    )

    await agent.initialize()
    await agent.start()

    agent.remember(
        content="Naveen is building AURA AI.",
        memory_type="project",
        importance=0.95,
    )

    memories = agent.get_recent()

    print()
    print("=" * 60)
    print("AURA MEMORIES")
    print("=" * 60)

    for memory in memories:
        print(
            f"[{memory.id}] "
            f"{memory.content} "
            f"(type={memory.memory_type}, "
            f"importance={memory.importance})"
        )

    await agent.stop()
    await agent.shutdown()


if __name__ == "__main__":
    asyncio.run(main())