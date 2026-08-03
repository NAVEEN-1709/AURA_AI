"""
Base Agent for AURA AI.

All agents inherit from this class.
"""

from abc import ABC, abstractmethod

from core.logger import logger


class BaseAgent(ABC):
    """
    Abstract base class for all AURA agents.
    """

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the agent."""

    @abstractmethod
    async def start(self) -> None:
        """Start the agent."""

    @abstractmethod
    async def stop(self) -> None:
        """Stop the agent."""

    @abstractmethod
    async def shutdown(self) -> None:
        """Shutdown the agent."""

    def log(self, message: str) -> None:
        """Write a log message prefixed with the agent name."""
        logger.info("[{}] {}", self.name, message)