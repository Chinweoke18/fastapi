"""add foreign to post table

Revision ID: 01fc1ecf2b81
Revises: 8885238f4b34
Create Date: 2023-06-10 08:23:35.034619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01fc1ecf2b81'
down_revision = '8885238f4b34'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
