from demo import message
from demo.log import get_logger
from fastapi import FastAPI

logger = get_logger("greet-FastAPI-logger")
app = FastAPI()


@app.get("/")
def root() -> dict:
    logger.info("The FastAPI root endpoint was called.")

    return {"message": message.hello_world()}
