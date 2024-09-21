from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.author import Author
from models.book import Book
from models.borrower import Borrower
from models.transaction import Transaction

# Set up the database
engine = create_engine('sqlite:///library.sqlite3')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_session():
    return session

