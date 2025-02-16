from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy import insert
import random

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

Session = sessionmaker(autoflush=False,bind=engine)

session = Session()

Base = declarative_base()

conn = engine.connect()

metadata = db.MetaData()



divisons = db.Table('divisons',metadata,db.Column("id", db.Integer, primary_key=True),db.Column("username",db.String),db.Column("email",db.String))

print(f'Table is {metadata.tables["divisons"]}')

stmnt = db.insert(divisons).values(id=random.randint(1,1001),username="Angelina",email='angelina@hollywood.com')
metadata.create_all(engine)
with engine.connect():
    conn.execute(stmnt)
    conn.commit()

with engine.connect() as conn:
    resultset = conn.execute(db.text('SELECT * FROM divisions'))
    rows = resultset.fetchall()

for row in rows:
    print(f' row is {row}')

