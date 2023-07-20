from demo import message
from demo.schema import Message
from fastapi import Body, FastAPI

from demo.database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/message/", response_model=int)
def create(content: str = Body()):
    return message.create(content)


@app.get("/message/{message_id}", response_model=Message)
def read(message_id: int):
    return message.read(message_id)


@app.put("/message/{message_id}", response_model=None)
def update(message_id: int, content: str = Body()):
    return message.update(message_id, content)


@app.post("/message/{message_id}", response_model=None)
def delete(message_id: int):
    return message.delete(message_id)
