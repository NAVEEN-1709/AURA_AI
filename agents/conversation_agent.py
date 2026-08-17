"""
AURA AI

Conversation Agent

Handles conversations between the user and AURA.
"""

from agents.base import BaseAgent
from core.logger import logger
from llm.models import ChatMessage, ChatRole
from llm.router import LLMRouter
from llm.session import ChatSession
from memory.agent import MemoryAgent


class ConversationAgent(BaseAgent):
    """
    Handles user conversations using the LLM Router
    and persistent Memory Agent.
    """

    def __init__(
        self,
        llm_router: LLMRouter,
        memory_agent: MemoryAgent,
    ) -> None:
        super().__init__("Conversation")

        self._llm_router = llm_router
        self._memory_agent = memory_agent

        self._system_prompt = (
            "You are AURA, a personal AI assistant running "
            "on the user's Windows computer. "
            "You are friendly, calm, professional, curious, "
            "and honest. "
            "You must never claim to have performed an action "
            "unless that action was actually executed by an "
            "available AURA tool. "
            "If you cannot perform an action yet, clearly say so. "
            "Do not pretend to have capabilities that have not "
            "been implemented."
        )

        self._session = ChatSession(
            system_prompt=self._system_prompt,
            max_messages=20,
        )

        logger.info(
            "Conversation Agent created."
        )

    async def initialize(self) -> None:
        """Initialize the Conversation Agent."""

        self.log(
            "Initializing Conversation Agent..."
        )

    async def start(self) -> None:
        """Start the Conversation Agent."""

        self.log(
            "Conversation Agent started."
        )

    async def stop(self) -> None:
        """Stop the Conversation Agent."""

        self.log(
            "Conversation Agent stopped."
        )

    async def shutdown(self) -> None:
        """Shutdown the Conversation Agent."""

        self.log(
            "Conversation Agent shutdown."
        )

    async def process_message(
        self,
        message: str,
    ) -> str:
        """
        Process a user message using conversation
        history and persistent memories.
        """

        if not message.strip():
            return (
                "I didn't catch that. "
                "Could you say that again?"
            )

        self.log(
            f"Received message: {message}"
        )

        # Let the Memory Agent inspect the user's message
        # for high-confidence long-term memories.
        self._memory_agent.process_user_message(
            message
        )

        # Add the user's message to short-term memory.
        self._session.add_user_message(
            message
        )

        # Retrieve recent persistent memories.
        memories = self._memory_agent.get_recent(
            limit=5
        )

        memory_context = ""

        if memories:
            memory_lines = [
                f"- {memory.content}"
                for memory in memories
            ]

            memory_context = (
                "\n\nRelevant memories about the user:\n"
                + "\n".join(memory_lines)
            )

        # Build messages for the LLM.
        messages = self._session.get_messages()

        # Add persistent memory as an additional
        # system-level context message.
        if memory_context:
            messages.insert(
                1,
                ChatMessage(
                    role=ChatRole.SYSTEM,
                    content=memory_context,
                ),
            )

        # Generate response.
        response = await self._llm_router.generate(
            messages=messages,
        )

        # Store assistant response in short-term memory.
        self._session.add_assistant_message(
            response.content
        )

        self.log(
            "Response generated using "
            f"{response.provider}/{response.model}"
        )

        return response.content