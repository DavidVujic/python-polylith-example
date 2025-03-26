from example import greeting, log
from example.greet_api import core

logger = log.get_logger("The DEV logger")
data = greeting.hello_world()

logger.info(data)


def start_local_for_repl_driven_development_with_jupyter_kernel():
    """Dev-only FastAPI startup.
    Important: only for REPL Driven Development using Jupyter kernel.

    This will start the app in an event loop. This is useful
    when running the app in a Jupyter kernel and connecting clients
    to the kernel.
    """

    import asyncio

    from example.message_api import core
    from uvicorn import Config, Server

    config = Config(core.app, host="127.0.0.1", port=8000)
    server = Server(config)

    loop = asyncio.get_running_loop()

    loop.create_task(server.serve())

    return loop
