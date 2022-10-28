"""add user table

Revision ID: 5dbcb0c67215
Revises: 44e7f45c8466
Create Date: 2022-10-27 17:49:47.883239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5dbcb0c67215'
down_revision = '44e7f45c8466'
branch_labels = None
depends_on = None


def upgrade():
	op.create_table('users', 
									sa.Column('id', sa.Integer(), nullable=False),
									sa.Column('email', sa.String(), nullable=False),
									sa.Column('password', sa.String(), nullable=False),
									sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
									sa.PrimaryKeyConstraint('id'),
									sa.UniqueConstraint('email')
									)
	pass


def downgrade():
	op.drop_table('users')
	pass

