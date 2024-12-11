"""[bot]merging heads

Revision ID: 363fdf7e6e5c
Revises: 94a53008bc5c, bd4d45c05be5
Create Date: 2024-12-02 12:19:37.264363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '363fdf7e6e5c'
down_revision = ('94a53008bc5c', 'bd4d45c05be5')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
