"""
AURA AI

Main Entry Point
"""

import asyncio

from core.orchestrator import Orchestrator


async def main() -> None:
    """
    Application entry point.
    """

    orchestrator = Orchestrator()

    await orchestrator.start()


if __name__ == "__main__":
    asyncio.run(main())