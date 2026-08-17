"""
AURA AI

Command Line Interface.

Provides a simple interactive interface for
communicating with AURA.
"""

from agents.conversation_agent import ConversationAgent


class CLI:
    """
    Interactive terminal interface for AURA.
    """

    def __init__(
        self,
        conversation_agent: ConversationAgent,
    ) -> None:
        self._conversation_agent = conversation_agent

    async def run(self) -> None:
        """
        Start the interactive chat loop.
        """

        print()
        print("=" * 60)
        print("                    AURA AI")
        print("=" * 60)
        print()
        print("Local AI: Ollama / llama3.2:3b")
        print("Type 'exit' or 'quit' to close AURA.")
        print()

        while True:
            try:
                user_input = input("You > ").strip()

            except (EOFError, KeyboardInterrupt):
                print()
                break

            if not user_input:
                continue

            if user_input.lower() in {
                "exit",
                "quit",
            }:
                print()
                print("AURA > Goodbye! 👋")
                break

            try:
                response = (
                    await self._conversation_agent
                    .process_message(user_input)
                )

                print()
                print(f"AURA > {response}")
                print()

            except Exception as exc:
                print()
                print(
                    "AURA > Sorry, I encountered an error "
                    "while processing that request."
                )
                print(f"Error: {exc}")
                print()