from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date
from sqlalchemy import String, Integer, DateTime


class Tithe(BaseModel):
    sum_general: float
    sum_children: float
    sum_family: float
    sum_other: float
    date_updated: date
    note: str

    class Config:
        orm_mode = True


