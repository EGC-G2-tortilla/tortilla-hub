"""empty message

Revision ID: 26242a811df2
Revises: 363fdf7e6e5c
Create Date: 2024-12-11 13:59:40.506957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26242a811df2'
down_revision = '363fdf7e6e5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ds_metrics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('average_features_per_model', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('constraints_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('max_depth', sa.Integer(), nullable=True))

    with op.batch_alter_table('fm_metrics', schema=None) as batch_op:
        batch_op.add_column(sa.Column('number_of_features', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('constraints_count', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('max_depth', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('variability', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fm_metrics', schema=None) as batch_op:
        batch_op.drop_column('variability')
        batch_op.drop_column('max_depth')
        batch_op.drop_column('constraints_count')
        batch_op.drop_column('number_of_features')

    with op.batch_alter_table('ds_metrics', schema=None) as batch_op:
        batch_op.drop_column('max_depth')
        batch_op.drop_column('constraints_count')
        batch_op.drop_column('average_features_per_model')

    # ### end Alembic commands ###
