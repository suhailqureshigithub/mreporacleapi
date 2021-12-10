from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.engine.url import URL
import cx_Oracle

cx_Oracle.init_oracle_client(
    lib_dir=r"C:\oraclexe\app\oracle\product\11.2.0\server\bin")

SQLALCHEMY_DATABASE_URL='sqlite:///./blog.db'
engine=create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

connect_url = URL(
    "oracle+cx_oracle",
    username="apps",
    password="apps",
    host="192.168.130.41",
    port="1521",
    database="prod"
)

oracleEngine =create_engine(connect_url)
oracleSessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=oracleEngine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_Oracledb():
    db=oracleSessionLocal()
    try:
        yield db
    finally:
        db.close()



