"""create posts table

Revision ID: 9f446b404e9a
Revises: 
Create Date: 2022-10-27 17:25:48.850749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f446b404e9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
									sa.Column('title', sa.String(), nullable=False))
	pass


def downgrade():
	op.drop_table('posts')
	pass
