"""empty message

Revision ID: 7420ed3b8cde
Revises: 7f8153afdfca
Create Date: 2019-09-29 23:05:50.394668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7420ed3b8cde'
down_revision = '7f8153afdfca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'admin_user', ['user_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'admin_user', type_='unique')
    # ### end Alembic commands ###
