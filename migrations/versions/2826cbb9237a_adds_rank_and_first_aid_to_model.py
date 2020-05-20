"""Adds rank and first_aid to model

Revision ID: 2826cbb9237a
Revises: 555eb51de372
Create Date: 2020-05-10 22:05:45.667783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2826cbb9237a'
down_revision = '555eb51de372'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_aid', sa.String(length=50), nullable=True))
    op.add_column('users', sa.Column('rank', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rank')
    op.drop_column('users', 'first_aid')
    # ### end Alembic commands ###
