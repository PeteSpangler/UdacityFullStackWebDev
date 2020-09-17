"""empty message

Revision ID: b19ab83ed403
Revises: cc4bfa0ea985
Create Date: 2020-09-17 09:12:24.624119

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b19ab83ed403'
down_revision = 'cc4bfa0ea985'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Shows', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.drop_column('Shows', 'upcoming')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('upcoming', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('Shows', 'start_time',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
