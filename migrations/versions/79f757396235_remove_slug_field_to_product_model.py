"""remove slug field to product model

Revision ID: 79f757396235
Revises: c050aa3236c5
Create Date: 2021-04-06 10:37:40.701357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79f757396235'
down_revision = 'c050aa3236c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'slug')
    op.drop_column('product', 'slug')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('slug', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    op.add_column('category', sa.Column('slug', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    # ### end Alembic commands ###