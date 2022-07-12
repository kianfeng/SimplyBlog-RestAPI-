from pydantic import BaseModel
from typing import List, Union


# class of customized pydantic model


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    #  let Pydantic model to read the data even if it is not a dict(make Pydantic model is compatible with ORMs)
    #  this is dict: id = data["id"], now we can get from attribute  id = data.id
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    password: str
    email: str


class User(BaseModel):
    name: str
    email: str


# 这里可以像https://fastapi.tiangolo.com/tutorial/sql-databases/ 里面一样只用一个User来做respond的display，但记得要加orm_mode
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    string: Union[str, None] = None