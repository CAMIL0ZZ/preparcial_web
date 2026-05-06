import os
from dotenv import load_dotenv
from sqlmodel import Session, create_engine, select
from model import Farmaco, Cliente

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

def create_db_and_tables():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)