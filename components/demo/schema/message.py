from pydantic import BaseModel


class Message(BaseModel):
    id: int
    content: str | None = None

    class Config:
        orm_mode = True
