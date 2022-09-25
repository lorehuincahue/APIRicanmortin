"""empty message

Revision ID: 3ec9ddef9110
Revises: 
Create Date: 2022-09-21 21:54:03.526963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ec9ddef9110'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('capitulos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('capitulos', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personajes', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('personajes'),
    sa.UniqueConstraint('personajes')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('fav_capitulos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('capitulos_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['capitulos_id'], ['capitulos.id'], ),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fav_personajes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personajes_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ),
    sa.ForeignKeyConstraint(['personajes_id'], ['personajes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_personajes')
    op.drop_table('fav_capitulos')
    op.drop_table('user')
    op.drop_table('personajes')
    op.drop_table('capitulos')
    # ### end Alembic commands ###