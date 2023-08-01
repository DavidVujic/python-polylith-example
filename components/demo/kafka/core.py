"""
In a Real-World scenario, you likely want to fetch the Kafka-specific
config depending on the running environment (such as environment variables for dev, test or prod).

In this simplistic example, the values returned from these functions are fixed.
"""


def fetch_default_config() -> dict:
    return {"bootstrap.servers": "localhost:9092"}


def fetch_consumer_config() -> dict:
    return {"group.id": "python_example_group_1", "auto.offset.reset": "earliest"}
