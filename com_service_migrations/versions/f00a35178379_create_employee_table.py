"""create employee table

Revision ID: f00a35178379
Revises:
Create Date: 2017-10-05 14:29:21.121236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f00a35178379'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'employee',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(60), nullable=False),
        sa.Column('designation', sa.String(60))
    )


def downgrade():
    op.drop_table('employee')
