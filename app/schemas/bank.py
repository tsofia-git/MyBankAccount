from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from datetime import date
from sqlalchemy import String, Integer, DateTime
from app.models.revenue import Revenue


class Bank(BaseModel):
    bank_code: int
    bank_name: str
    sum: float
    update_date: date

    # revenue: List[Revenue]

    class Config:
        orm_mode = True
