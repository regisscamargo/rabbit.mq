from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

STR_DATABASE = (
    f"mysql+pymysql://root:abcBolinhas@172.18.32.1/abcBolinhas?charset=utf8mb4"
)

engine = create_engine(STR_DATABASE, echo=True)
Session = sessionmaker(bind=engine)
# para trabalhar com tabelas
Base = declarative_base()
