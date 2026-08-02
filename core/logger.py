"""
AURA AI Logger

Centralized logging configuration using Loguru.
"""

from pathlib import Path
from loguru import logger
import sys

# Create logs directory if it doesn't exist
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Console output
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan> - "
           "<level>{message}</level>",
)

# File output
logger.add(
    LOG_DIR / "aura.log",
    level="DEBUG",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    encoding="utf-8",
)

__all__ = ["logger"]