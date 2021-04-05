"""add courier model

Revision ID: 7ea223fbcdc3
Revises: b1dbb9a7328e
Create Date: 2021-03-24 14:14:51.561513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ea223fbcdc3'
down_revision = 'b1dbb9a7328e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=25), nullable=True),
    sa.Column('last_name', sa.String(length=25), nullable=True),
    sa.Column('contact_phone', sa.String(length=10), nullable=False),
    sa.Column('vk_id', sa.Integer(), nullable=True),
    sa.Column('tg_id', sa.Integer(), nullable=True),
    sa.Column('fb_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courier')
    # ### end Alembic commands ###