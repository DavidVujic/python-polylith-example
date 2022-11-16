import json

from demo import message
from demo.log import get_logger

logger = get_logger("messages-lambda-logger")


def handler(event: dict, context: dict) -> dict:
    logger.info("The Lambda handler was invoked.")

    body = {"messages": [message.hello_world()]}

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
