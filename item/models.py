import sqlalchemy
from sqlalchemy import Integer

metadata = sqlalchemy.MetaData()


item_table = sqlalchemy.Table(
    'item',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, index=True, unique=True),
    sqlalchemy.Column('user', Integer, sqlalchemy.ForeignKey('users_table.c.id')),
    sqlalchemy.Column('name', sqlalchemy.String(255), nullable=False, unique=True),
    sqlalchemy.Column('description', sqlalchemy.Text),
    sqlalchemy.Column('price', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('amount', sqlalchemy.Integer),
)
