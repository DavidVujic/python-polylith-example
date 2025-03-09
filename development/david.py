from example import greeting, log
from example.greet_api import core
from uvicorn import Config, Server
import asyncio

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)

config = Config(core.app, host="127.0.0.1", port=8000)
server = Server(config)

def start_local():
    loop = asyncio.get_running_loop()

    loop.create_task(server.serve())
