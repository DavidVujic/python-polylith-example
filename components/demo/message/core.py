from demo.database import Session
from demo.database.message import crud


def create(content: str) -> int:
    with Session() as session:
        return crud.create(session, content)


def read(message_id: int):
    with Session() as session:
        return crud.read(session, message_id)


def update(message_id: int, content: str):
    with Session() as session:
        return crud.update(session, message_id, content)


def delete(message_id: int):
    with Session() as session:
        return crud.delete(session, message_id)
