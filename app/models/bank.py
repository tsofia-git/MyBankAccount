from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.db.database import Base
from sqlalchemy.orm import relationship


class Bank(Base):
    __tablename__ = "bank"

    id = Column(Integer, primary_key=True, index=True)
    bank_code = Column(Integer, primary_key=True)
    bank_name = Column(String(80))
    sum = Column(Float, unique=False, index=False)
    update_date = Column(DateTime(timezone=True), server_default=func.now())
    revenue = relationship("Revenue")
