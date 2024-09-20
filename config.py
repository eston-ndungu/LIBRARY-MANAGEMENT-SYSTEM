from models.author import Author, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Engine = create_engine('sqlite:///library.sqlite3')

Base.metadata.create_all(Engine)

Session = sessionmaker(bind=Engine)
session = Session()


def get_session():
    return session

