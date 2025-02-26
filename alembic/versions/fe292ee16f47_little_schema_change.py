"""Little Schema Change

Revision ID: fe292ee16f47
Revises: 8efdc9b79978
Create Date: 2025-02-26 12:33:19.659735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'fe292ee16f47'
down_revision: Union[str, None] = '8efdc9b79978'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'about',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=300),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'about',
               existing_type=sa.String(length=300),
               type_=mysql.TEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###
