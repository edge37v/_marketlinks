"""empty message

Revision ID: 1b16124b8e8a
Revises: 
Create Date: 2021-03-02 09:47:34.302443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b16124b8e8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('save_count', sa.Integer(), nullable=True),
    sa.Column('card', sa.JSON(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('username', sa.Unicode(), nullable=True),
    sa.Column('show_email', sa.Boolean(), nullable=True),
    sa.Column('hide_location', sa.Boolean(), nullable=True),
    sa.Column('location', sa.JSON(), nullable=True),
    sa.Column('distance', sa.Float(), nullable=True),
    sa.Column('openby', sa.DateTime(), nullable=True),
    sa.Column('closedby', sa.DateTime(), nullable=True),
    sa.Column('online', sa.Boolean(), nullable=True),
    sa.Column('images', sa.Unicode(), nullable=True),
    sa.Column('image', sa.Unicode(), nullable=True),
    sa.Column('customer_code', sa.Unicode(), nullable=True),
    sa.Column('subscribed', sa.Boolean(), nullable=True),
    sa.Column('visible', sa.Boolean(), nullable=True),
    sa.Column('email', sa.Unicode(), nullable=True),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('about', sa.Unicode(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    op.create_table('item',
    sa.Column('tags', sa.JSON(), nullable=True),
    sa.Column('save_count', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('image', sa.Unicode(), nullable=True),
    sa.Column('images', sa.JSON(), nullable=True),
    sa.Column('itype', sa.Unicode(), nullable=True),
    sa.Column('price', sa.Unicode(), nullable=True),
    sa.Column('name', sa.Unicode(), nullable=True),
    sa.Column('description', sa.Unicode(), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('saved_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('saved_items',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('item', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item'], ['item.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('saved_items')
    op.drop_table('saved_users')
    op.drop_table('item')
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
