"""empty message

Revision ID: 9e4060ae9dd3
Revises: 0396a5ed0d5f
Create Date: 2023-06-02 17:24:33.728554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e4060ae9dd3'
down_revision = '0396a5ed0d5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('title_crew', schema=None) as batch_op:
        batch_op.alter_column('directors',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=50000),
               existing_nullable=True)
        batch_op.alter_column('writers',
               existing_type=sa.VARCHAR(length=5000),
               type_=sa.String(length=50000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('title_crew', schema=None) as batch_op:
        batch_op.alter_column('writers',
               existing_type=sa.String(length=50000),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)
        batch_op.alter_column('directors',
               existing_type=sa.String(length=50000),
               type_=sa.VARCHAR(length=5000),
               existing_nullable=True)

    # ### end Alembic commands ###