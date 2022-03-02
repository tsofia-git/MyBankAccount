from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.orm import relationship


class Revenue(Base):
    __tablename__ = "revenue"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, unique=False, index=False)
    source = Column(String(80), unique=False, index=False)
    bank_id = Column(Integer, ForeignKey("bank.id"))
    date_revenue = Column(DateTime(timezone=True), server_default=func.now())
    regular = Column(Boolean, default=0)
    note = Column(String(80))
