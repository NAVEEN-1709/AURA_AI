"""
AURA AI

Memory Agent

Coordinates persistent memory operations and automatic
memory extraction.
"""

from agents.base import BaseAgent
from core.logger import logger
from memory.extractor import MemoryExtractor
from memory.manager import MemoryManager


class MemoryAgent(BaseAgent):
    """
    Agent responsible for managing AURA's persistent memory.
    """

    def __init__(
        self,
        memory_manager: MemoryManager,
    ) -> None:
        super().__init__("Memory")

        self._memory_manager = memory_manager
        self._extractor = MemoryExtractor()

        logger.info(
            "Memory Agent created."
        )

    async def initialize(self) -> None:
        """Initialize the Memory Agent."""

        self.log(
            "Initializing Memory Agent..."
        )

    async def start(self) -> None:
        """Start the Memory Agent."""

        self.log(
            "Memory Agent started."
        )

    async def stop(self) -> None:
        """Stop the Memory Agent."""

        self.log(
            "Memory Agent stopped."
        )

    async def shutdown(self) -> None:
        """Shutdown the Memory Agent."""

        self.log(
            "Memory Agent shutdown."
        )

    def remember(
        self,
        content: str,
        memory_type: str = "general",
        importance: float = 0.5,
    ) -> None:
        """Store a memory explicitly."""

        memory = self._memory_manager.remember(
            content=content,
            memory_type=memory_type,
            importance=importance,
        )

        if memory is not None:
            self.log(
                f"Remembered: {content}"
            )

    def process_user_message(
        self,
        message: str,
    ) -> None:
        """
        Analyze a user message and automatically store
        high-confidence memories.
        """

        candidates = self._extractor.extract(
            message
        )

        for candidate in candidates:
            memory = self._memory_manager.remember(
                content=candidate.content,
                memory_type=candidate.memory_type,
                importance=candidate.importance,
            )

            if memory is not None:
                self.log(
                    "Automatically remembered: "
                    f"{candidate.content}"
                )

    def get_recent(
        self,
        limit: int = 10,
    ):
        """Retrieve recent memories."""

        return self._memory_manager.get_recent(
            limit=limit
        )