from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import date
from sqlalchemy import String, Integer, DateTime


class Revenue(BaseModel):
    amount: float
    regular: Optional[bool]
    source: str
    id_bank: int
    date_revenue: date
    note: Optional[str]

    class Config:
        orm_mode = True
