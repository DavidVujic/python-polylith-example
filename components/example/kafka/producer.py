"""
A simplistic example implementation of a Kafka Producer,
with the basics as described in the Confluent Python Client Getting Started guides.
"""

from functools import cache

from confluent_kafka import Producer
from example import log
from example.kafka.core import fetch_default_config, is_enabled
from example.kafka.parser import parse_message

logger = log.get_logger("Kafka-Producer-logger")


def _acked(err, msg):
    if err:
        logger.error(err)
        return

    topic, key, value = parse_message(msg)

    logger.info(f"Produced: topic={topic}: key={key} value={value}")


@cache
def get_producer() -> Producer:
    logger.info("a new instance of a Kafka Producer")

    config = fetch_default_config()

    return Producer(config)


def produce(topic: str, key: str, value: str) -> None:
    if not is_enabled():
        return

    producer = get_producer()

    producer.produce(topic, value, key, callback=_acked)

    producer.poll(10000)
    producer.flush()
