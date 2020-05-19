"""Adds role enum

Revision ID: 555eb51de372
Revises: ff3b8e2ed0b2
Create Date: 2020-05-10 21:55:16.554046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '555eb51de372'
down_revision = 'ff3b8e2ed0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('app_role', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'app_role')
    # ### end Alembic commands ###
