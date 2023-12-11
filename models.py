from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    status = Column(String)
    owner = Column(String)


engine = create_engine("postgresql+psycopg://postgres:postgres@localhost:9998/postgres")
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)