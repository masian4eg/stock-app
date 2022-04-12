from fastapi import APIRouter

from item import stock

routes = APIRouter()

routes.include_router(stock.router, prefix='/stock')
