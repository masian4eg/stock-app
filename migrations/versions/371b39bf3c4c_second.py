"""Second

Revision ID: 371b39bf3c4c
Revises: d569226ec6ea
Create Date: 2022-04-11 14:14:13.359694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '371b39bf3c4c'
down_revision = 'd569226ec6ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_item_id'), 'item', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_item_id'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###
