"""Add patient table

Revision ID: 002
Revises:
Create Date: 2021-06-02 14:31:33.813799

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade():
    # 🥸 This is where you add patient table.
    pass


def downgrade():
    # 🥸 This is where you drop it.
    pass
