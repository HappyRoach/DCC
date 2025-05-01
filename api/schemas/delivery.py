import typing
from datetime import datetime

from pydantic import BaseModel


class DeliveryBase(BaseModel):
    weight: int
    dimensions: str
    address_in: str
    address_out: str
    datetime_in: datetime
    datetime_out: datetime
    transport_id: int

    class Config:
        orm_mode = True


class DeliveryCreate(DeliveryBase):
    pass


class DeliveryUpdate(BaseModel):
    weight: typing.Optional[int] = None
    dimensions: typing.Optional[str] = None
    address_in: typing.Optional[str] = None
    address_out: typing.Optional[str] = None
    datetime_in: typing.Optional[datetime] = None
    datetime_out: typing.Optional[datetime] = None
    transport_id: typing.Optional[int] = None
    status: typing.Optional[str] = None

    class Config:
        orm_mode = True


class DeliveryGet(DeliveryBase):
    id: int
    user_delivery_id: int
    status: str

    class Config:
        orm_mode = True 