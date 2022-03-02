from datetime import datetime
from typing import Optional, Any

from fastapi import APIRouter, Depends
from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app.bl import curd_revenue
import app.models.revenue
import app.schemas.revenue

router = APIRouter(
    prefix="/revenue",
    tags=["revenue"]
)


@router.post('/create_revenue', status_code=201)
def create_revenue(request: app.schemas.revenue.Revenue, db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    print('PPPPPPPPPPPPPPPPPPPPPPPPPPP')
    db_revenue = curd_revenue.revenue.create(db_postgres=db_postgres, request=request)
    return db_revenue


@router.get('/all', status_code=201)
def get_all_revenue(limit=10, sort_by: Optional[str] = None, sort_dir: Optional[str] = "desc",
                    db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    revenue = db_postgres.query(app.models.revenue.Revenue)
    if sort_by:
        direction = desc if sort_dir == 'desc' else asc
        revenue = revenue.order_by(direction(getattr(app.models.revenue.Revenue, sort_by)))
    revenue = revenue.limit(limit).all()

    return revenue


@router.get('/get_revenue_by_date/{by_date}', status_code=201)
def get_revenue_by_date(by_date: datetime, limit=10, sort_by: Optional[str] = None, sort_dir: Optional[str] = "desc",
                        db_postgres: Session = Depends(app.db.database.get_db)) -> Any:
    print('000000000000000000000000000000000000000000000000000')
    # revenue = db_postgres.query(models.revenue.Revenue).filter(
    #     models.revenue.Revenue.date_revenue.strftime("%m/%d/%Y") == by_date)
    # if sort_by:
    #     direction = desc if sort_dir == 'desc' else asc
    #     revenue = revenue.order_by(direction(getattr(models.revenue.Revenue, sort_by)))
    # revenue = revenue.limit(limit).all()
    #
    # return revenue
    return '3333333333333333333'
