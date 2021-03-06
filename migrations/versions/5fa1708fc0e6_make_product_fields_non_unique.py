"""make product fields non-unique

Revision ID: 5fa1708fc0e6
Revises: 35e79394cf1c
Create Date: 2021-03-26 14:43:39.767607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5fa1708fc0e6'
down_revision = '35e79394cf1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('product_slug_key', 'product', type_='unique')
    op.drop_index('ix_product_name', table_name='product')
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.create_index('ix_product_name', 'product', ['name'], unique=True)
    op.create_unique_constraint('product_slug_key', 'product', ['slug'])
    # ### end Alembic commands ###
