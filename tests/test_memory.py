"""
Test AURA persistent memory.
"""

from memory.database import MemoryDatabase
from memory.manager import MemoryManager


def main() -> None:
    database = MemoryDatabase(
        database_path="database/test_memory.db"
    )

    memory_manager = MemoryManager(
        database=database
    )

    memory = memory_manager.remember(
        content="My name is Naveen.",
        memory_type="personal",
        importance=0.9,
    )

    print()
    print("=" * 60)
    print("MEMORY STORED")
    print("=" * 60)

    print(f"ID: {memory.id}")
    print(f"Content: {memory.content}")
    print(f"Type: {memory.memory_type}")
    print(f"Importance: {memory.importance}")

    print()
    print("=" * 60)
    print("RECENT MEMORIES")
    print("=" * 60)

    memories = memory_manager.get_recent()

    for item in memories:
        print(
            f"[{item.id}] "
            f"{item.content} "
            f"(importance={item.importance})"
        )


if __name__ == "__main__":
    main()