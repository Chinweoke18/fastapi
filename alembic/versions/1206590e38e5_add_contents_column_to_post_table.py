"""add contents column to post table

Revision ID: 1206590e38e5
Revises: f5a6d3c31797
Create Date: 2023-06-10 07:12:05.206888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1206590e38e5'
down_revision = 'f5a6d3c31797'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
