"""
AURA AI

Main application entry point.
"""

import asyncio

from core.logger import logger
from core.orchestrator import Orchestrator
from ui.cli import CLI


async def main() -> None:
    """
    Start and run AURA.
    """

    orchestrator = Orchestrator()

    try:
        await orchestrator.start()

        cli = CLI(
            conversation_agent=(
                orchestrator.conversation_agent
            )
        )

        await cli.run()

    except KeyboardInterrupt:
        logger.warning(
            "AURA interrupted by user."
        )

    except Exception:
        logger.exception(
            "Fatal AURA error."
        )

    finally:
        await orchestrator.stop()
        await orchestrator.shutdown()


if __name__ == "__main__":
    asyncio.run(main())