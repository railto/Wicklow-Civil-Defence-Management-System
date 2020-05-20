"""Adds timestamps

Revision ID: 8f39f79ca308
Revises: 7f8366332b04
Create Date: 2020-05-14 13:13:49.456552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f39f79ca308'
down_revision = '7f8366332b04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search_radioassignments', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('search_radioassignments', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('searches', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('searches', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('searches', 'updated_at')
    op.drop_column('searches', 'created_at')
    op.drop_column('search_radioassignments', 'updated_at')
    op.drop_column('search_radioassignments', 'created_at')
    # ### end Alembic commands ###
