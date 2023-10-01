from typing import Any, Tuple


def parse_message(msg: Any) -> Tuple[str, str, str]:
    topic = msg.topic()
    key = msg.key().decode("utf-8")
    value = msg.value().decode("utf-8")

    return topic, key, value
