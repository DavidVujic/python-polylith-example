import json
import os

from demo.hello_world import greet
from demo.my_logger import getLogger

logger = getLogger("my-lambda-logger")


def handler(event, context):
    logger.info("The Lambda handler has been triggered.")

    region = os.environ.get("AWS_REGION", "No region is set")
    mesage = greet()
    body = {"region": region, "message": message}

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }
