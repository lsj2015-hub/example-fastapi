"""add last few columns to post table

Revision ID: 9e2980902630
Revises: c1830577eb64
Create Date: 2022-10-27 19:08:39.170542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e2980902630'
down_revision = 'c1830577eb64'
branch_labels = None
depends_on = None


def upgrade():
	op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=True, server_default='TRUE'))
	op.add_column('posts', sa.Column(
		'created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.text('NOW()')
	))
	pass


def downgrade():
	op.drop_column('posts', 'created_at')
	op.drop_column('posts', 'published')
	pass
