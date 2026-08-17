"""
AURA AI

Memory Models
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Memory:
    """
    Represents a stored memory.
    """

    id: int | None
    content: str
    memory_type: str
    importance: float
    created_at: datetime
    last_accessed_at: datetime