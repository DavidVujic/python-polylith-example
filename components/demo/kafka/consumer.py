from functools import cache
from typing import Callable

from confluent_kafka import Consumer
from demo import log
from demo.kafka.core import fetch_consumer_config, fetch_default_config
from demo.kafka.parser import parse_message

logger = log.get_logger("Kafka-Consumer-logger")


@cache
def _get_consumer() -> Consumer:
    logger.info("a new instance of a Kafka Consumer")

    config = fetch_default_config() | fetch_consumer_config()

    return Consumer(config)


def consume(topic: str, callback: Callable) -> None:
    consumer = _get_consumer()

    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                logger.error(msg.error())
            else:
                topic, key, value = parse_message(msg)
                callback(topic, key, value)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
