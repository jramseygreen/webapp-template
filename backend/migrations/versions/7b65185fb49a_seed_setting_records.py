"""seed setting records

Revision ID: 7b65185fb49a
Revises: d05e7fe129c3
Create Date: 2024-04-27 16:45:19.516567

"""
from alembic import op
import sqlalchemy as sa
from secrets import token_urlsafe

# revision identifiers, used by Alembic.
revision = '7b65185fb49a'
down_revision = 'd05e7fe129c3'
branch_labels = None
depends_on = None


def upgrade():
    connection = op.get_bind()

    # Insert record into the setting table
    random_key = token_urlsafe(32)
    connection.execute(sa.Table('setting', sa.MetaData(), autoload_with=connection).insert().values(name='JWT_SECRET_KEY', value=random_key, description=None, type='str', is_sensitive=True))
    connection.execute(sa.Table('setting', sa.MetaData(), autoload_with=connection).insert().values(name='REGISTRATION_ENABLED', value='true', description='Toggle allowing new users to register', type='bool', is_sensitive=False))
    connection.execute(sa.Table('setting', sa.MetaData(), autoload_with=connection).insert().values(name='FORCE_LOGIN', value='false', description='To view any page, the user must be logged in', type='bool', is_sensitive=False))


def downgrade():
    connection = op.get_bind()

    # Delete JWT_SECRET_KEY record from the config table
    connection.execute(
        sa.Table('setting', sa.MetaData(), autoload_with=connection)
        .delete()
        .where(sa.text("name = 'JWT_SECRET_KEY'"))
    )

    # Delete REGISTRATION_ENABLED record from the config table
    connection.execute(
        sa.Table('setting', sa.MetaData(), autoload_with=connection)
        .delete()
        .where(sa.text("name = 'REGISTRATION_ENABLED'"))
    )

    # Delete FORCE_LOGIN record from the config table
    connection.execute(
        sa.Table('setting', sa.MetaData(), autoload_with=connection)
        .delete()
        .where(sa.text("name = 'FORCE_LOGIN'"))
    )
