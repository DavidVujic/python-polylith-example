from example import log, message
from example.schema import Message
from fastapi import Body, FastAPI

from example.database import Base, engine

logger = log.get_logger("message-FastAPI-logger")
app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/message/", response_model=int)
def create(content: str = Body()):
    logger.info(f"Creating a message with content={content}")

    return message.create(content)


@app.get("/message/{message_id}", response_model=Message)
def read(message_id: int):
    logger.info(f"Fetching message with id={message_id}")

    return message.read(message_id)


@app.put("/message/{message_id}", response_model=None)
def update(message_id: int, content: str = Body()):
    logger.info(f"Updating message with id={message_id}")

    return message.update(message_id, content)


@app.post("/message/{message_id}", response_model=None)
def delete(message_id: int):
    logger.info(f"Deleting message with id={message_id}")

    return message.delete(message_id)
