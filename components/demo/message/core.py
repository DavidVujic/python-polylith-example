import json

from demo import kafka
from demo.database import Session
from demo.database.message import crud
from demo.dictionaries import pick


def create(content: str) -> int:
    with Session.begin() as session:
        data = crud.create(session, content)
        return data.id


def read(message_id: int):
    with Session.begin() as session:
        return vars(crud.read(session, message_id))


def update(message_id: int, content: str) -> None:
    with Session.begin() as session:
        existing = crud.read(session, message_id)

        if not existing:
            raise ValueError()

        return crud.update(session, existing, content)


def delete(message_id: int) -> None:
    with Session.begin() as session:
        return crud.delete(session, message_id)


def notify(message_id: int) -> None:
    data = read(message_id)
    message = pick(data, {"id", "content"})

    key = str(message["id"])
    value = json.dumps(message)

    kafka.producer.produce("message", key, value)
