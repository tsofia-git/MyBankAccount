
# Core packages
from fastapi import FastAPI
from app.db.database import engine

from app.api import api_revenue, api_expense, api_bank
from app.models import revenue, expense, bank

revenue.Base.metadata.create_all(bind=engine)
expense.Base.metadata.create_all(bind=engine)
bank.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(api_revenue.router)
app.include_router(api_expense.router)
app.include_router(api_bank.router)


#
# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# # core packages
# from typing import Optional
#
# import uvicorn
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# # set the type of objects that app uses
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None
#
#
# @app.get('/')
# def index():
#     return {'hello': 'kkkkkkkkkkkkkkkkkk'}
#
#
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_price": item.price, "item_id": item_id}
#
#
# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
