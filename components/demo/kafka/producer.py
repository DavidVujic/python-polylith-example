from confluent_kafka import Producer
from demo import log
from demo.kafka.core import fetch_default_config
from demo.kafka.parser import parse_message


logger = log.get_logger("Kafka-Producer-logger")
config = fetch_default_config()
producer = Producer(config)


def _delivery_callback(err, msg):
    if err:
        logger.error(err)
        return

    topic, key, value = parse_message(msg)

    logger.info(f"Produced: topic={topic}: key={key} value={value}")


def produce(topic: str, key: str, value: str) -> None:
    producer.produce(topic, value, key, callback=_delivery_callback)

    producer.poll(10000)
    producer.flush()
