"""
AURA AI

Event Bus

Provides publish-subscribe communication
between independent modules.
"""

from collections import defaultdict
from collections.abc import Callable
from typing import Any

from core.logger import logger


class EventBus:
    """
    Simple publish-subscribe event bus.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[Callable[[Any], None]]] = defaultdict(list)

        logger.info("Event Bus initialized.")

    def subscribe(
        self,
        event_name: str,
        callback: Callable[[Any], None],
    ) -> None:
        """
        Register a callback for an event.
        """
        self._subscribers[event_name].append(callback)

        logger.info(
            "Subscribed '{}' to event '{}'",
            callback.__name__,
            event_name,
        )

    def publish(
        self,
        event_name: str,
        data: Any = None,
    ) -> None:
        """
        Publish an event to all subscribers.
        """

        logger.info("Publishing event '{}'", event_name)

        for callback in self._subscribers[event_name]:
            callback(data)