"""
AURA AI

LLM Data Models

Defines common data structures used by
all language model providers.
"""

from dataclasses import dataclass, field
from enum import Enum


class ChatRole(str, Enum):
    """Supported conversation roles."""

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(slots=True)
class ChatMessage:
    """Represents one message in a conversation."""

    role: ChatRole
    content: str


@dataclass(slots=True)
class ChatResponse:
    """Standard response returned by an LLM provider."""

    content: str
    provider: str
    model: str
    usage: dict[str, int] = field(default_factory=dict)