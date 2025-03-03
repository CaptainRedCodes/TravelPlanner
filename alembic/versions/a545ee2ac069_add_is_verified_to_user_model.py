"""Add is_verified to User model

Revision ID: a545ee2ac069
Revises: 
Create Date: 2025-02-18 22:54:52.719321

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a545ee2ac069'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('users', sa.Column('is_verified', sa.Boolean(), nullable=False))
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=50),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.alter_column('users', 'password',
               existing_type=mysql.VARCHAR(length=100),
               type_=sa.String(length=100),
               existing_nullable=False)
    op.alter_column('users', 'created_at',
               existing_type=mysql.DATETIME(),
               type_=sa.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'created_at',
               existing_type=sa.TIMESTAMP(timezone=True),
               type_=mysql.DATETIME(),
               nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
    op.alter_column('users', 'password',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(length=50),
               existing_nullable=False)
    op.drop_column('users', 'is_verified')
    # ### end Alembic commands ###
