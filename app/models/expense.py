from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.db.database import Base


class Expense(Base):
    __tablename__ = "expense"

    expense_id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, unique=False, index=False)
    id_bank = Column(Integer)
    date_expense = Column(DateTime(timezone=True), server_default=func.now())
    target = Column(String(80), unique=False, index=False)
    note = Column(String(80))
