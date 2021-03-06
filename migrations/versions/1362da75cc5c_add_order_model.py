"""add order model

Revision ID: 1362da75cc5c
Revises: 358ccc7d1b46
Create Date: 2021-03-24 17:12:00.148639

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.


revision = '1362da75cc5c'
down_revision = '358ccc7d1b46'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('delivered_at', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    status_enum = postgresql.ENUM('processed', 'unprocessed', name='orderstatusenum')
    status_enum.create(op.get_bind())
    op.add_column('order', sa.Column('status', status_enum, nullable=False))

    payment_method_enum = postgresql.ENUM('cash', 'card', name='paymentmethodenum')
    payment_method_enum.create(op.get_bind())
    op.add_column('order', sa.Column('payment_method', payment_method_enum, nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
