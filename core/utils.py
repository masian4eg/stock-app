from fastapi import HTTPException
from sqlalchemy import select, desc

from core.db import database
from item.models import item_table
from user.models import users_table
from item import schemas as item_schema

seller = users_table.c.is_seller


async def get_items(page: int):

    max_per_page = 10
    query = (
        select(
            [
                item_table.c.id,
                item_table.c.name,
                item_table.c.description,
                item_table.c.price,
                item_table.c.amount,
            ]
        )
        .order_by(desc(item_table.c.name))
        .limit(max_per_page)
    )

    return await database.fetch_all(query)


async def create_item(item: item_schema.ItemBase):

    if seller is False:
        raise HTTPException(status_code=403, detail='You are not seller')
    else:
        query = (
            item_table.insert()
            .values(
                name=item.name,
                description=item.description,
                price=item.price,
                amount=item.amount,
            )
            .returning(
                item_table.c.name,
                item_table.c.description,
                item_table.c.price,
                item_table.c.amount,
            )
        )

        item = await database.fetch_one(query)  # Here product is Record object
        item = dict(zip(item, item.values()))  # Record to dict goes here

        return item


async def item_buy(pcs: int, item: item_schema.ItemBase):

    if seller:
        raise HTTPException(status_code=403, detail='You are seller')

    if item_table.c.amount < pcs:
        raise HTTPException(status_code=404, detail='Not enough items')
    else:
        query = (
            item_table.update()
            .set(item_table.c.amount - pcs)
        )

        return await database.fetch_one(query)
