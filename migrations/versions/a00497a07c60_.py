"""empty message

Revision ID: a00497a07c60
Revises: 
Create Date: 2019-12-28 16:47:21.366157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a00497a07c60'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_key', sa.String(length=280), nullable=False),
    sa.Column('value', sa.String(length=280), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice')
    # ### end Alembic commands ###
