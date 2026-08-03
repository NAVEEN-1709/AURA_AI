"""
AURA AI

Main Entry Point
"""

from core.config_loader import get_settings
from core.logger import logger


def print_banner() -> None:
    settings = get_settings()

    print("=" * 60)
    print(f"           {settings.app.name}")
    print(f"           Version {settings.app.version}")
    print("=" * 60)


def startup() -> None:
    settings = get_settings()

    logger.info("Starting {}", settings.app.name)
    logger.info("Environment: {}", settings.app.environment)
    logger.info("Default LLM: {}", settings.llm.default_provider)
    logger.info("Wake Word: {}", settings.speech.wake_word)

    logger.success("Configuration Loaded")
    logger.success("AURA is online")


def main() -> None:
    print_banner()

    startup()

    print()
    print("Hello! I'm AURA.")
    print("How can I help you today?")


if __name__ == "__main__":
    main()