from sqlalchemy import select, desc

from core.db import database
from .models import item_table


async def get_products(page: int):
    max_per_page = 10
    query = (
        select(
            [
                item_table.c.id,
                item_table.c.created_date,
                item_table.c.title,
                item_table.c.quantity,
                item_table.c.user_id,
                item_table.c.name.label('user_name'),
            ]
        )
        .order_by(desc(item_table.c.created_date))
        .limit(max_per_page)
    )

    return await database.fetch_all(query)
