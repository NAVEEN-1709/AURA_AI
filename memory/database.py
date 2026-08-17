"""
AURA AI

Memory Database

SQLite persistence layer for AURA memories.
"""

import sqlite3
from pathlib import Path

from core.logger import logger


class MemoryDatabase:
    """
    Handles SQLite storage for AURA memories.
    """

    def __init__(
        self,
        database_path: str = "database/aura_memory.db",
    ) -> None:
        self._database_path = Path(database_path)

        self._database_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._initialize_database()

    def _connect(self) -> sqlite3.Connection:
        """
        Create a SQLite database connection.
        """

        connection = sqlite3.connect(
            self._database_path
        )

        connection.row_factory = sqlite3.Row

        return connection

    def _initialize_database(self) -> None:
        """
        Create the memories table if it doesn't exist.
        """

        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content TEXT NOT NULL,
                    memory_type TEXT NOT NULL,
                    importance REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    last_accessed_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

        logger.info(
            "Memory database initialized: {}",
            self._database_path,
        )

    def add_memory(
        self,
        content: str,
        memory_type: str,
        importance: float,
        created_at: str,
        last_accessed_at: str,
    ) -> int:
        """
        Store a memory and return its ID.
        """

        with self._connect() as connection:
            cursor = connection.execute(
                """
                INSERT INTO memories (
                    content,
                    memory_type,
                    importance,
                    created_at,
                    last_accessed_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    content,
                    memory_type,
                    importance,
                    created_at,
                    last_accessed_at,
                ),
            )

            connection.commit()

            return int(cursor.lastrowid)
    
    def memory_exists(
        self,
        content: str,
    ) -> bool:
        """
        Check whether an identical memory already exists.
        """

        with self._connect() as connection:
            cursor = connection.execute(
                """
                SELECT 1
                FROM memories
                WHERE LOWER(content) = LOWER(?)
                LIMIT 1
                """,
                (content,),
            )

            return cursor.fetchone() is not None

    def get_recent_memories(
        self,
        limit: int = 10,
    ) -> list[sqlite3.Row]:
        """
        Return the most recently created memories.
        """

        with self._connect() as connection:
            cursor = connection.execute(
                """
                SELECT *
                FROM memories
                ORDER BY created_at DESC
                LIMIT ?
                """,
                (limit,),
            )

            return cursor.fetchall()