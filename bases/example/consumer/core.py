from example import kafka, log

logger = log.get_logger("Consumer-app-logger")


def parse_message(topic: str, key: str, value: str) -> None:
    logger.info(f"Consumed message with topic={topic}, key={key}, value={value}")


def main() -> None:
    topic = "message"
    kafka.consumer.consume(topic, parse_message)
