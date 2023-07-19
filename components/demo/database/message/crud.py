from typing import cast

from demo.database.message.model import Message
from sqlalchemy import select
from sqlalchemy.orm import Session


def create(session: Session, content: str) -> int:
    data = Message(content=content)

    session.add(data)

    return data.id


def read(session: Session, message_id: int) -> Message:
    query = select(Message).where(Message.id == message_id)

    return cast(Message, session.execute(query).one())


def update(session: Session, message_id: int, content: str) -> None:
    existing = read(session, message_id)

    existing.content = content

    session.add(existing)


def delete(session: Session, message_id: int) -> None:
    existing = read(session, message_id)

    session.delete(existing)
