from datetime import datetime
from config_postgress_alchemy import postgres_sql
from sqlalchemy import PrimaryKeyConstraint
# from sqlalchemy_utils import database_exists, create_database
# from config_postgres_alchemy import postgres_sql as settings
from sqlalchemy import Table, Column, Integer, String, Float, TIMESTAMP, MetaData, Boolean, Identity, BigInteger
from sqlalchemy import create_engine

url = f"postgresql://{postgres_sql['user']}:{postgres_sql['password']}@{postgres_sql['host']}:{postgres_sql['port']}" \
      f"/{postgres_sql['db']}"

engine_fin = create_engine(url, pool_size=5, echo=False)

meta = MetaData()
start_time = datetime.now()

user = Table('users', meta,
             Column('id_user', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('nickname', String(10), nullable=False),
             Column('pass_word', String(10), nullable=False),
             PrimaryKeyConstraint('id_user', name='id_user_pk'))

boss = Table('boss', meta,
             Column('id_boss', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('nome', String(10), nullable=False),
             PrimaryKeyConstraint('id_boss', name='id_boss_pk'))

business = Table('business', meta,
             Column('id_business', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('nome', String(10), nullable=False),
             Column('id_boss',Integer,nullable=False),
             Column('descr',String(100),nullable = True),
             PrimaryKeyConstraint('id_business', name='id_business_pk'))

jobs = Table('jobs', meta,
             Column('id_jobs', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('id_business', String(10), nullable=False),
             Column('data_start',TIMESTAMP,nullable=False),
             Column('data_end',TIMESTAMP,nullable=False),
             Column('h_payment',Float,nullable=False),
             Column('descr',String(100),nullable = True),
             PrimaryKeyConstraint('id_jobs', name='id_jobs_pk'))

works = Table('works',meta,
             Column('id_works', Integer, Identity("always"), nullable=False, primary_key=True),
             Column('id_jobs', String(10), nullable=False),
             Column('data',TIMESTAMP,nullable=False),
             Column('entry',TIMESTAMP,nullable=False),
             Column('exit',TIMESTAMP,nullable=False),
             Column('descr',String(100),nullable = True),
             PrimaryKeyConstraint('id_works', name='id_works_pk'))

meta.create_all(engine_fin)
