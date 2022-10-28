"""add content column to posts table

Revision ID: 44e7f45c8466
Revises: 9f446b404e9a
Create Date: 2022-10-27 17:39:32.856651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44e7f45c8466'
down_revision = '9f446b404e9a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
