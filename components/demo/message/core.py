from demo.database import Session
from demo.database.message import crud


def create(content: str) -> int:
    with Session.begin() as session:
        data = crud.create(session, content)
        return data.id


def read(message_id: int):
    with Session.begin() as session:
        return vars(crud.read(session, message_id))


def update(message_id: int, content: str):
    with Session.begin() as session:
        return crud.update(session, message_id, content)


def delete(message_id: int):
    with Session.begin() as session:
        return crud.delete(session, message_id)
