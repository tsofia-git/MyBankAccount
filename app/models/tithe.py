from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql import func
from app.db.database import Base


class Tithe(Base):
    __tablename__ = "tens"

    tithes_id = Column(Integer, primary_key=True, index=True)
    sum_general = Column(Float, unique=False, index=False, default=0)
    sum_children = Column(Float, unique=False, index=False, default=0)
    sum_family = Column(Float, unique=False, index=False, default=0)
    sum_other = Column(Float, unique=False, index=False, default=0)
    date_updated = Column(DateTime(timezone=True), server_default=func.now())
    note = Column(String(80))
