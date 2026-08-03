import asyncio

from agents.base import BaseAgent


class DemoAgent(BaseAgent):
    async def initialize(self):
        self.log("Initialized")

    async def start(self):
        self.log("Started")

    async def stop(self):
        self.log("Stopped")

    async def shutdown(self):
        self.log("Shutdown")


async def main():
    agent = DemoAgent("Demo")

    await agent.initialize()
    await agent.start()
    await agent.stop()
    await agent.shutdown()


asyncio.run(main())