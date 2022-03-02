# set the db connection
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.db import settings


host_server = 'localhost'
db_server_port = '5432'
database_name = 'postgres'
db_username = 'postgres'
db_password = 'postgres'
ssl_mode = 'Prefer'
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username,db_password, host_server, db_server_port, database_name, ssl_mode)

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE['username']}:{settings.DATABASE['password']}@localhost/{settings.DATABASE['db_name']}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
