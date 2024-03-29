"""empty message

Revision ID: 7f8153afdfca
Revises: 
Create Date: 2019-09-24 23:49:09.204980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f8153afdfca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=25), nullable=False),
    sa.Column('user_mail', sa.String(length=25), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user')
    # ### end Alembic commands ###
