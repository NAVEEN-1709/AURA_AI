"""
AURA AI

Memory Extractor

Detects potentially important user statements that should
be persisted as long-term memories.
"""

from dataclasses import dataclass
import re


@dataclass(slots=True)
class MemoryCandidate:
    """Represents a possible long-term memory."""

    content: str
    memory_type: str
    importance: float


class MemoryExtractor:
    """
    Extracts explicit, high-confidence memories from
    user messages.

    This first implementation intentionally uses deterministic
    rules. Later we can add an LLM-based extractor as a second
    stage for more complex memories.
    """

    _PATTERNS: tuple[
        tuple[str, str, float, str],
        ...
    ] = (
        (
            r"\bmy name is\s+(.+?)(?:[.!?]|$)",
            "personal",
            1.0,
            "My name is {value}.",
        ),
        (
            r"\bi(?:'m| am)\s+(.+?)(?:[.!?]|$)",
            "personal",
            0.8,
            "I am {value}.",
        ),
        (
            r"\bmy favorite\s+(.+?)\s+is\s+(.+?)(?:[.!?]|$)",
            "preference",
            0.9,
            "My favorite {key} is {value}.",
        ),
        (
            r"\bi prefer\s+(.+?)(?:[.!?]|$)",
            "preference",
            0.8,
            "I prefer {value}.",
        ),
        (
            r"\bi like\s+(.+?)(?:[.!?]|$)",
            "preference",
            0.7,
            "I like {value}.",
        ),
        (
            r"\bi don't like\s+(.+?)(?:[.!?]|$)",
            "preference",
            0.8,
            "I don't like {value}.",
        ),
        (
            r"\bi am working on\s+(.+?)(?:[.!?]|$)",
            "project",
            0.9,
            "I am working on {value}.",
        ),
        (
            r"\bi'm working on\s+(.+?)(?:[.!?]|$)",
            "project",
            0.9,
            "I am working on {value}.",
        ),
        (
            r"\bi am building\s+(.+?)(?:[.!?]|$)",
            "project",
            0.9,
            "I am building {value}.",
        ),
        (
            r"\bi'm building\s+(.+?)(?:[.!?]|$)",
            "project",
            0.9,
            "I am building {value}.",
        ),
        (
            r"\bi use\s+(.+?)(?:[.!?]|$)",
            "preference",
            0.6,
            "I use {value}.",
        ),
    )

    def extract(
        self,
        message: str,
    ) -> list[MemoryCandidate]:
        """
        Extract high-confidence memories from a user message.
        """

        text = message.strip()

        if not text:
            return []

        candidates: list[MemoryCandidate] = []

        for pattern, memory_type, importance, template in (
            self._PATTERNS
        ):
            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE,
            )

            if not match:
                continue

            groups = [
                group.strip()
                for group in match.groups()
            ]

            if len(groups) == 1:
                content = template.format(
                    value=groups[0]
                )

            elif len(groups) == 2:
                content = template.format(
                    key=groups[0],
                    value=groups[1],
                )

            else:
                continue

            candidates.append(
                MemoryCandidate(
                    content=content,
                    memory_type=memory_type,
                    importance=importance,
                )
            )

        return self._deduplicate(candidates)

    @staticmethod
    def _deduplicate(
        candidates: list[MemoryCandidate],
    ) -> list[MemoryCandidate]:
        """Remove duplicate memory candidates."""

        unique: dict[str, MemoryCandidate] = {}

        for candidate in candidates:
            key = candidate.content.lower()

            if key not in unique:
                unique[key] = candidate

        return list(unique.values())