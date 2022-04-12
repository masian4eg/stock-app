"""user table

Revision ID: efce8788c110
Revises: 371b39bf3c4c
Create Date: 2022-04-11 14:27:17.580140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efce8788c110'
down_revision = '371b39bf3c4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('is_activ', sa.Boolean(), nullable=True),
    sa.Column('is_seller', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=True)
    op.add_column('item', sa.Column('user', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'item', 'user', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'item', type_='foreignkey')
    op.drop_column('item', 'user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
