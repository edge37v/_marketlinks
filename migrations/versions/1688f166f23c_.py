"""empty message

Revision ID: 1688f166f23c
Revises: 5955a633681f
Create Date: 2021-01-15 21:17:52.396022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1688f166f23c'
down_revision = '5955a633681f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distance', sa.Float(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('distance', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('distance')

    with op.batch_alter_table('item', schema=None) as batch_op:
        batch_op.drop_column('distance')

    # ### end Alembic commands ###
