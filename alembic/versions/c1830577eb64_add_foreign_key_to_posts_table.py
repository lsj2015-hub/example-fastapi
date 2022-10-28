"""add foreign-key to posts table

Revision ID: c1830577eb64
Revises: 5dbcb0c67215
Create Date: 2022-10-27 18:02:00.538210

"""
from tkinter import CASCADE
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1830577eb64'
down_revision = '5dbcb0c67215'
branch_labels = None
depends_on = None


def upgrade():
	op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
	op.create_foreign_key('post_users_fk', source_table='posts', referent_table="users", 
	local_cols=['owner_id'], remote_cols=['id'], ondelete=CASCADE)
	pass


def downgrade():
	op.drop_constraint('post_users_fk', table_name="posts")
	op.drop_column('posts', 'owner_id')
	pass