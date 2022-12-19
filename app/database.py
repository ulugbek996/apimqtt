from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from databases import Database


SQLALCHEMY_DATABASE_URL ='postgresql://postgres:12345@apimqtt_postgres_1:5432/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
database = Database(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, future=True)
Base = declarative_base()
conn = MongoClient('mongodb://apimqtt_mongo_1:27017')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()