from pydantic import BaseModel
import typing


class UserCreate(BaseModel):
    login: str
    password: str
    role_id: int

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    user_id: int | str
    role_id: int | str

    class Config:
        orm_mode = True


class Login(BaseModel):
    login: str
    password: str


class RegularUserCreate(BaseModel):
    login: str
    name: typing.Optional[str] = None
    password: str

    class Config:
        orm_mode = True
