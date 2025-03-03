"""initial 3

Revision ID: eaf39072bf62
Revises: 62a266006763
Create Date: 2025-02-23 23:02:25.634979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'eaf39072bf62'
down_revision: Union[str, None] = '62a266006763'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'id',
               existing_type=mysql.VARCHAR(length=36),
               type_=sa.Integer(),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('trips', 'id',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=36),
               existing_nullable=False,
               autoincrement=True)
    # ### end Alembic commands ###
