from typing import Optional

from fastapi import FastAPI

from demo.hello_world import greet
from demo.my_logger import getLogger

logger = getLogger("my-FastAPI-logger")


app = FastAPI()


@app.get("/")
def root():
    logger.info("The FastAPI root endpoint was called.")

    return {"message": greet()}
