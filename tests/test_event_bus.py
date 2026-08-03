from core.event_bus import EventBus


def greet(data):
    print(f"Hello {data['name']}!")


bus = EventBus()

bus.subscribe("greeting", greet)

bus.publish("greeting", {"name": "Naveen"})