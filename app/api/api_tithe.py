from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.models.tithe

router = APIRouter(
    prefix="/tithe",
    tags=["tithe"]
)


@router.get('/all_tithes', status_code=201)
def get_all_tithes(limit=10, db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    tithes = db_postgres.query(app.models.tithe.Tithes)
    tithes = tithes.limit(limit).all()

    return tithes


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
