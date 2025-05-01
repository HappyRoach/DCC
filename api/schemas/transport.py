import typing

from pydantic import BaseModel


class TransportBase(BaseModel):
    capacity: int
    dimensions: str

    class Config:
        orm_mode = True


class TransportCreate(TransportBase):
    pass


class TransportUpdate(BaseModel):
    capacity: typing.Optional[int] = None
    dimensions: typing.Optional[str] = None

    class Config:
        orm_mode = True


class TransportGet(TransportBase):
    id: int

    class Config:
        orm_mode = True 