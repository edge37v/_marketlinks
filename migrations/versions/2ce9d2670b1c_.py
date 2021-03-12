"""empty message

Revision ID: 2ce9d2670b1c
Revises: 0491846dee7a
Create Date: 2021-03-11 19:40:57.585288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ce9d2670b1c'
down_revision = '0491846dee7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.drop_index('ix_user_token', table_name='user')
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=False)
    op.drop_constraint('user_email_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.create_index('ix_user_token', 'user', ['token'], unique=True)
    op.drop_column('event', 'end_date')
    # ### end Alembic commands ###
