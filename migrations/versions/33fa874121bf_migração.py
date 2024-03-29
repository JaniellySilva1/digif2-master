"""Migração

Revision ID: 33fa874121bf
Revises: 2e95828b00a6
Create Date: 2022-03-21 15:29:37.881617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33fa874121bf'
down_revision = '2e95828b00a6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('receitas', sa.Column('id_receita', sa.Integer(), nullable=False))
    op.drop_column('receitas', 'id_despesa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('receitas', sa.Column('id_despesa', sa.INTEGER(), nullable=False))
    op.drop_column('receitas', 'id_receita')
    # ### end Alembic commands ###
