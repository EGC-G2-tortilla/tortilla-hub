"""Merging migrations

Revision ID: 8bb175a68811
Revises: 6f5857a1b32d, a063a912d659, b40c8e066fc2
Create Date: 2024-11-12 17:45:21.992328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bb175a68811'
down_revision = ('6f5857a1b32d', 'a063a912d659', 'b40c8e066fc2')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
