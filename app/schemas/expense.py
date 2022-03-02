from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date
from sqlalchemy import String, Integer, DateTime


class Expense(BaseModel):
    amount: float
    regular: Optional[bool]
    target: str
    id_bank: int
    date_expense: date
    note: str

    class Config:
        orm_mode = True


