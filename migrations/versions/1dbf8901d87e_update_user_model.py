"""update user model

Revision ID: 1dbf8901d87e
Revises: efce8788c110
Create Date: 2022-04-11 16:53:22.586105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dbf8901d87e'
down_revision = 'efce8788c110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(length=72), nullable=False))
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    op.add_column('user', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_index('ix_user_id', table_name='user')
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.drop_column('user', 'password')
    op.drop_column('user', 'is_activ')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_activ', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user', 'is_verified')
    op.drop_column('user', 'is_superuser')
    op.drop_column('user', 'is_active')
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###