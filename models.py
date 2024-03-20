from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

Base = declarative_base()
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    id_no=Column(Integer())
