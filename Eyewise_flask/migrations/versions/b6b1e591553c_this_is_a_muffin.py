"""This is a muffin

Revision ID: b6b1e591553c
Revises: 4aacc7417aa7
Create Date: 2018-05-14 21:10:44.409085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6b1e591553c'
down_revision = '4aacc7417aa7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('colour', sa.String(length=15), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'colour')
    # ### end Alembic commands ###
