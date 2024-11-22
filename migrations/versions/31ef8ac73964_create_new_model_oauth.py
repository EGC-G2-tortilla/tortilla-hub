"""create_new_model_oauth

Revision ID: 31ef8ac73964
Revises: 001
Create Date: 2024-11-07 20:13:29.422015

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '31ef8ac73964'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('o_auth_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('provider_name', sa.String(length=50), nullable=True),
    sa.Column('provider_user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    op.drop_table('o_auth_provider')
    # ### end Alembic commands ###