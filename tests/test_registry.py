import asyncio

from agents.base import BaseAgent
from agents.registry import AgentRegistry


class DemoAgent(BaseAgent):
    async def initialize(self):
        pass

    async def start(self):
        pass

    async def stop(self):
        pass

    async def shutdown(self):
        pass


async def main():
    registry = AgentRegistry()

    agent = DemoAgent("Demo")

    registry.register(agent)

    print(registry.list_agents())


asyncio.run(main())