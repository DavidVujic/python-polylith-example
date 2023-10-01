from example.database.message.model import Message
from sqlalchemy import select
from sqlalchemy.orm import Session


def create(session: Session, content: str) -> Message:
    data = Message(content=content)

    session.add(data)
    session.flush()

    return data


def read(session: Session, message_id: int) -> Message | None:
    query = select(Message).where(Message.id == message_id)

    return session.execute(query).scalar()


def update(session: Session, existing: Message, content: str) -> None:
    existing.content = content

    session.add(existing)


def delete(session: Session, message_id: int) -> None:
    existing = read(session, message_id)

    session.delete(existing)
