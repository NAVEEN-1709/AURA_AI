"""
Conversation Agent for AURA AI.
"""

from agents.base import BaseAgent


class ConversationAgent(BaseAgent):
    """
    Handles user conversations.
    """

    def __init__(self) -> None:
        super().__init__("Conversation")

    async def initialize(self) -> None:
        self.log("Initializing Conversation Agent...")

    async def start(self) -> None:
        self.log("Conversation Agent started.")

    async def stop(self) -> None:
        self.log("Conversation Agent stopped.")

    async def shutdown(self) -> None:
        self.log("Conversation Agent shutdown.")

    async def process_message(self, message: str) -> str:
        """
        Process a user message.

        Currently returns a placeholder response.
        """

        self.log(f"Received message: {message}")

        return (
            "Hello! I'm AURA. "
            "My AI brain is still under development."
        )