from typing import Optional, Any

from fastapi import APIRouter, Depends
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

import app.models.expense
import app.schemas.expense

router = APIRouter(
    prefix="/expense",
    tags=["expense"]
)


@router.post('/create_expense', status_code=201)
def create(request: app.schemas.expense.Expense, db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    db_expense = app.models.expense.Expense()
    db_expense.amount = request.amount
    db_expense.target = request.target
    db_expense.id_bank = request.id_bank
    db_expense.note = request.note

    db_postgres.add(db_expense)
    db_postgres.commit()
    db_postgres.refresh(db_expense)

    return db_expense


@router.get('/all_expense', status_code=201, response_model=app.schemas.expense.Expense)
def get_all_expense(limit=10, sort_by: Optional[str] = None, sort_dir: Optional[str] = "desc",
                    db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    expense = db_postgres.query(app.models.expense.Expense)
    if sort_by:
        direction = desc if sort_dir == 'desc' else asc
        expense = expense.order_by(direction(getattr(app.models.expense.Expense, sort_by)))
    expense = expense.limit(limit).all()

    return expense


# @router.get('/get_revenue_by_date/{by_date}', status_code=201)
# def get_revenue_by_date(by_date: datetime, limit=10, sort_by: Optional[str] = None, sort_dir: Optional[str] = "desc",
#                         db_postgres: Session = Depends(db.database.get_db)) -> Any:
#     print('000000000000000000000000000000000000000000000000000')
#     # revenue = db_postgres.query(models.revenue.Revenue).filter(
#     #     models.revenue.Revenue.date_revenue.strftime("%m/%d/%Y") == by_date)
#     # if sort_by:
#     #     direction = desc if sort_dir == 'desc' else asc
#     #     revenue = revenue.order_by(direction(getattr(models.revenue.Revenue, sort_by)))
#     # revenue = revenue.limit(limit).all()
#     #
#     # return revenue
#     return '3333333333333333333'
