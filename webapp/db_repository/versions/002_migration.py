from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
pibot = Table('pibot', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=35)),
    Column('location', String(length=35)),
    Column('operational', SmallInteger, default=ColumnDefault(0)),
    Column('net_address', String(length=16)),
)

tour = Table('tour', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', DateTime),
    Column('deadline', DateTime),
    Column('user_id', Integer),
    Column('pibot_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['pibot'].create()
    post_meta.tables['tour'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['pibot'].drop()
    post_meta.tables['tour'].drop()
