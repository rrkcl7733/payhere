from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class AccountBase(BaseModel):
    money: Optional[int] = None
    memo: Optional[str] = None


class AccountCreate(AccountBase):
    pass


class AccountUpdate(AccountBase):
    pass


class AccountList(AccountBase):

    class Config:
        orm_mode = True