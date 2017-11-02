"""empty message

Revision ID: e6ec08ef7e33
Revises: 9609ba577312
Create Date: 2017-10-31 18:44:18.273632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6ec08ef7e33'
down_revision = '9609ba577312'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('average', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'average')
    # ### end Alembic commands ###