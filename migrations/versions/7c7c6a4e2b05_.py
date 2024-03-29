"""empty message

Revision ID: 7c7c6a4e2b05
Revises: 9eab1343f1dd
Create Date: 2023-06-02 17:16:33.922475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c7c6a4e2b05'
down_revision = '9eab1343f1dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('title_crew', schema=None) as batch_op:
        batch_op.alter_column('directors',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=1000),
               existing_nullable=True)
        batch_op.alter_column('writers',
               existing_type=sa.VARCHAR(length=500),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('title_crew', schema=None) as batch_op:
        batch_op.alter_column('writers',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)
        batch_op.alter_column('directors',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###
