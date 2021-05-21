"""data file table

Revision ID: 8fc4a730f13b
Revises: 
Create Date: 2021-05-21 18:19:17.478577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fc4a730f13b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('file_name', sa.String(length=100), nullable=True),
    sa.Column('file_type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_file')
    # ### end Alembic commands ###
