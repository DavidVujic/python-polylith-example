import functions_framework
from example import greeting
from example.log import get_logger

logger = get_logger("greet-gcp-function-logger")


@functions_framework.http
def handler(_request):
    return greeting.hello_world()
