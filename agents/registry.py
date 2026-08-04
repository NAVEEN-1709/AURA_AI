"""
Agent Registry.
"""

from agents.base import BaseAgent
from core.logger import logger


class AgentRegistry:

    def __init__(self):
        self._agents: dict[str, BaseAgent] = {}

        logger.info("Agent Registry initialized.")

    def register(self, agent: BaseAgent):
        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' already exists."
            )

        self._agents[agent.name] = agent

        logger.info("Registered '{}'", agent.name)

    def get(self, name: str) -> BaseAgent:
        return self._agents[name]

    def list_agents(self):
        return list(self._agents.keys())

    async def initialize_all(self):
        logger.info("Initializing all agents...")

        for agent in self._agents.values():
            await agent.initialize()

    async def start_all(self):
        logger.info("Starting all agents...")

        for agent in self._agents.values():
            await agent.start()

    async def stop_all(self):
        logger.info("Stopping all agents...")

        for agent in self._agents.values():
            await agent.stop()

    async def shutdown_all(self):
        logger.info("Shutting down all agents...")

        for agent in self._agents.values():
            await agent.shutdown()