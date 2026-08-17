"""
AURA AI

Orchestrator

Coordinates AURA's core systems and agents.
"""

from agents.conversation_agent import ConversationAgent
from agents.registry import AgentRegistry
from core.config_loader import Settings, get_settings
from core.event_bus import EventBus
from core.logger import logger
from llm.providers.ollama_provider import OllamaProvider
from llm.router import LLMRouter
from memory.agent import MemoryAgent
from memory.database import MemoryDatabase
from memory.manager import MemoryManager


class Orchestrator:
    """
    Coordinates all major AURA components.
    """

    def __init__(self) -> None:
        """Create AURA's core infrastructure."""

        logger.info("Creating Orchestrator...")

        # Configuration
        self.settings: Settings = get_settings()

        # Core infrastructure
        self.event_bus = EventBus()
        self.registry = AgentRegistry()

        # LLM infrastructure
        self.ollama_provider = OllamaProvider(
            model="llama3.2:3b"
        )

        self.llm_router = LLMRouter(
            providers={
                "ollama": self.ollama_provider,
            },
            default_provider="ollama",
        )

        # Persistent memory infrastructure
        self.memory_database = MemoryDatabase(
            database_path="database/aura_memory.db"
        )

        self.memory_manager = MemoryManager(
            database=self.memory_database
        )

        # Agents
        self.memory_agent = MemoryAgent(
            memory_manager=self.memory_manager
        )

        self.conversation_agent = ConversationAgent(
            llm_router=self.llm_router,
            memory_agent=self.memory_agent,
        )

        logger.success(
            "Orchestrator created successfully."
        )

    async def initialize(self) -> None:
        """
        Initialize AURA components and agents.
        """

        logger.info("Initializing AURA...")

        # Register agents.
        self.registry.register(
            self.memory_agent
        )

        self.registry.register(
            self.conversation_agent
        )

        # Initialize all agents.
        await self.registry.initialize_all()

        logger.success(
            "All agents initialized."
        )

    async def start(self) -> None:
        """
        Start the AURA application.
        """

        logger.info("Starting AURA...")

        await self.initialize()

        await self.registry.start_all()

        logger.success(
            "AURA started successfully."
        )

    async def stop(self) -> None:
        """
        Stop all running agents.
        """

        logger.info("Stopping AURA...")

        await self.registry.stop_all()

        logger.success(
            "AURA stopped."
        )

    async def shutdown(self) -> None:
        """
        Shutdown AURA gracefully.
        """

        logger.info("Shutting down AURA...")

        await self.registry.shutdown_all()

        logger.success(
            "AURA shutdown complete."
        )