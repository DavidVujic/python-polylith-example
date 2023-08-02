"""
In a Real-World scenario, you likely want to fetch the Kafka-specific
configs depending on the running environment (such as environment variables for dev, test or prod).

In this simplistic example, values returned from these functions are fixed.
"""
import os


def fetch_default_config() -> dict:
    return {"bootstrap.servers": "localhost:9092"}


def fetch_consumer_config() -> dict:
    return {"group.id": "python_example_group_1", "auto.offset.reset": "earliest"}


def is_enabled() -> bool:
    """Check if Kafka is enabled or not.

    Note:
    This is to keep the example code simplistic,
    being able to run the CRUD code without a running Kafka server.
    """
    return os.environ.get("kafka", "") == "enabled"
