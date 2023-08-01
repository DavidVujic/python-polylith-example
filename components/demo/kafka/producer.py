"""
A simplistic example implementation of a Kafka Producer,
with the basics as described in the Confluent Python Client Getting Started guides.
"""

from functools import cache

from confluent_kafka import Producer
from demo import log
from demo.kafka.core import fetch_default_config
from demo.kafka.parser import parse_message

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
    producer = get_producer()

    producer.produce(topic, value, key, callback=_acked)

    producer.poll(10000)
    producer.flush()
