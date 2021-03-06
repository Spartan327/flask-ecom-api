"""add cart_product  model

Revision ID: ac36a514f889
Revises: 80af27ad948c
Create Date: 2021-03-28 15:28:12.196668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac36a514f889'
down_revision = '80af27ad948c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['restaurant_product_id'], ['restaurant_product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_product_cart_id'), 'cart_product', ['cart_id'], unique=False)
    op.create_index(op.f('ix_cart_product_restaurant_product_id'), 'cart_product', ['restaurant_product_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cart_product_restaurant_product_id'), table_name='cart_product')
    op.drop_index(op.f('ix_cart_product_cart_id'), table_name='cart_product')
    op.drop_table('cart_product')
    # ### end Alembic commands ###
