"""add user table

Revision ID: 8885238f4b34
Revises: 1206590e38e5
Create Date: 2023-06-10 07:17:25.234042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8885238f4b34'
down_revision = '1206590e38e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
