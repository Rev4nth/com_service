"""add column joined date

Revision ID: 769f1e2bb965
Revises: f00a35178379
Create Date: 2017-10-05 14:31:03.784493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '769f1e2bb965'
down_revision = 'f00a35178379'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('employee', sa.Column('joined_date', sa.DateTime))


def downgrade():
    op.drop_column('employee')
