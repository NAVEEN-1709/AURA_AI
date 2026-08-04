"""
AURA AI

Orchestrator

Coordinates all core systems and agents.
"""

from agents.registry import AgentRegistry
from core.config_loader import Settings, get_settings
from core.event_bus import EventBus
from core.logger import logger
from agents.conversation_agent import ConversationAgent


class Orchestrator:
    """
    Coordinates all AURA components.
    Responsible for creating and managing the core systems.
    """

    def __init__(self) -> None:
        """
        Create all core components.
        """

        logger.info("Creating Orchestrator...")

        # Load application settings
        self.settings: Settings = get_settings()

        # Create Event Bus
        self.event_bus = EventBus()

        # Create Agent Registry
        self.registry = AgentRegistry()

        logger.success("Orchestrator created successfully.")

    async def initialize(self) -> None:
        """
        Initialize all core systems.
        """

        logger.info("Initializing AURA...")

        logger.info(
            "Application : {} {}",
            self.settings.app.name,
            self.settings.app.version,
        )

        logger.info(
            "Environment : {}",
            self.settings.app.environment,
        )

        logger.info(
            "Default LLM : {}",
            self.settings.llm.default_provider,
        )

        logger.info(
            "Wake Word   : {}",
            self.settings.speech.wake_word,
        )
        logger.success("Configuration loaded successfully.")
        logger.success("Core systems initialized.")

    async def start(self) -> None:
        """
        Start the AURA application.
        """
        logger.info("Starting AURA...")
        await self.initialize()
        logger.success("AURA started successfully.")

    async def shutdown(self) -> None:
        """
        Shutdown AURA gracefully.
        """
        logger.info("Shutting down AURA...")
        logger.success("AURA shutdown complete.")

    async def initialize(self) -> None:
        logger.info("Initializing AURA...")
        conversation = ConversationAgent()
        self.registry.register(conversation)
        await self.registry.initialize_all()
        await self.registry.start_all()
        logger.success("All agents started.")