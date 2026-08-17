"""
AURA AI

Memory Manager
"""

from datetime import datetime, timezone

from core.logger import logger
from memory.database import MemoryDatabase
from memory.models import Memory


class MemoryManager:
    """
    High-level interface for AURA memory.
    """

    def __init__(
        self,
        database: MemoryDatabase,
    ) -> None:
        self._database = database

        logger.info(
            "Memory Manager initialized."
        )

    def remember(
        self,
        content: str,
        memory_type: str = "general",
        importance: float = 0.5,
    ) -> Memory | None:
        """
        Store a new memory unless an identical memory
        already exists.
        """

        if self._database.memory_exists(content):
            logger.info(
                "Duplicate memory ignored: {}",
                content,
            )
            return None

        now = datetime.now(timezone.utc)

        memory_id = self._database.add_memory(
            content=content,
            memory_type=memory_type,
            importance=importance,
            created_at=now.isoformat(),
            last_accessed_at=now.isoformat(),
        )

        memory = Memory(
            id=memory_id,
            content=content,
            memory_type=memory_type,
            importance=importance,
            created_at=now,
            last_accessed_at=now,
        )

        logger.info(
            "Memory stored: {}",
            content,
        )

        return memory

    def get_recent(
        self,
        limit: int = 10,
    ) -> list[Memory]:
        """
        Retrieve recent memories.
        """

        rows = self._database.get_recent_memories(
            limit=limit
        )

        memories: list[Memory] = []

        for row in rows:
            memories.append(
                Memory(
                    id=row["id"],
                    content=row["content"],
                    memory_type=row["memory_type"],
                    importance=row["importance"],
                    created_at=datetime.fromisoformat(
                        row["created_at"]
                    ),
                    last_accessed_at=datetime.fromisoformat(
                        row["last_accessed_at"]
                    ),
                )
            )

        return memories