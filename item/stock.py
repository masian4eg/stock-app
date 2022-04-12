from fastapi import APIRouter

from core import utils as item_util
from .schemas import ItemCreate, ItemBase

router = APIRouter()


@router.get('/items')
async def item_list(page: int = 5):
    items = await item_util.get_items(page)
    return {'result': items}


@router.post('/items', response_model=ItemBase)
async def create_item(item: ItemCreate):
    item = await item_util.create_item(item)
    return item
