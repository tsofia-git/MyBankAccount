from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import String
from sqlalchemy.orm import Session

import app.schemas.bank
from app import models
from app.models.bank import Bank

router = APIRouter(
    prefix="/bank",
    tags=["bank"]
)


@router.get('/status_all', status_code=201, response_model=app.schemas.bank.Bank)
def get_status_bank(db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    bank = db_postgres.query(models.bank.Bank).all()

    return bank


@router.post('/create_bank', status_code=201)
def create_bank(request: app.schemas.bank.Bank, db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    db_bank = Bank()
    db_bank.bank_code = request.bank_code
    db_bank.bank_name = request.bank_name
    db_bank.sum = request.sum
    db_bank.update_date = request.update_date

    db_postgres.add(db_bank)
    db_postgres.commit()
    db_postgres.refresh(db_bank)

    return db_bank

# @router.get('/status_bank_by_name/{name}', status_code=201, response_model=app.schemas.bank.Bank)
# def get_status_of_bank_by_name(name: String, db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
#   bank = db_postgres.query(models.bank.Bank).filter(models.bank.Bank.bank_name == name).first()
#  if not bank:
#     raise HTTPException(status_code=404, detail=f"bank #{name} not found")

# return bank
