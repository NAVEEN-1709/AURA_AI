"""
AURA AI
Artificial Universal Responsive Assistant

Main Entry Point
"""

from datetime import datetime

from core.logger import logger


def print_banner() -> None:
    """Display startup banner."""
    print("=" * 60)
    print("                     AURA AI")
    print("      Artificial Universal Responsive Assistant")
    print("=" * 60)


def startup() -> None:
    """Initialize application."""
    logger.info("Starting AURA")
    logger.info(f"Startup Time: {datetime.now()}")
    logger.info("Loading configuration...")
    logger.info("Initializing core systems...")
    logger.success("AURA is online.")


def main() -> None:
    print_banner()

    startup()

    print()
    print("Hello! I'm AURA.")
    print("How can I help you today?")


if __name__ == "__main__":
    main()