"""
Agent Registry for AURA AI.

Responsible for registering and managing all agents.
"""

from typing import Dict

from agents.base import BaseAgent
from core.logger import logger


class AgentRegistry:
    """
    Stores and manages all registered agents.
    """

    def __init__(self) -> None:
        self._agents: Dict[str, BaseAgent] = {}

        logger.info("Agent Registry initialized.")

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent.
        """
        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' is already registered."
                )
        self._agents[agent.name] = agent
        logger.info("Registered agent '{}'", agent.name)

    def get(self, name: str) -> BaseAgent:
        """
        Retrieve an agent by name.
        """

        return self._agents[name]

    def list_agents(self) -> list[str]:
        """
        Return all registered agent names.
        """
        return list(self._agents.keys())