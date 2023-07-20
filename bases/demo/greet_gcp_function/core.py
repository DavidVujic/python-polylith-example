import functions_framework
from demo import greeting
from demo.log import get_logger

logger = get_logger("greet-gcp-function-logger")


@functions_framework.http
def handler(_request):
    return greeting.hello_world()
