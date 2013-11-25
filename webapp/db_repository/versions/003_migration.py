from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tour = Table('tour', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date', DateTime),
    Column('deadline', DateTime),
    Column('user_id', Integer),
    Column('pibot_id', Integer),
)

tour = Table('tour', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('start', DateTime),
    Column('finish', DateTime),
    Column('user_id', Integer),
    Column('pibot_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tour'].columns['date'].drop()
    pre_meta.tables['tour'].columns['deadline'].drop()
    post_meta.tables['tour'].columns['finish'].create()
    post_meta.tables['tour'].columns['start'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tour'].columns['date'].create()
    pre_meta.tables['tour'].columns['deadline'].create()
    post_meta.tables['tour'].columns['finish'].drop()
    post_meta.tables['tour'].columns['start'].drop()
