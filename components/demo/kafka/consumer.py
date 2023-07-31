from confluent_kafka import Consumer
from demo import log
from demo.kafka.core import fetch_consumer_config, fetch_default_config
from demo.kafka.parser import parse_message

logger = log.get_logger("Kafka-Consumer-logger")
config = fetch_default_config() | fetch_consumer_config()
consumer = Consumer(config)


def consume(topic: str) -> None:
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                logger.info("Waiting...")
            elif msg.error():
                logger.error(msg.error())
            else:
                topic, key, value = parse_message(msg)

                logger.info(f"Consumed: topic={topic}: key={key} value={value}")
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
