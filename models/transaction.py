from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.base import Base

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    borrower_id = Column(Integer, ForeignKey('borrowers.id'))
    checkout_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=True)

    book = relationship('Book', back_populates='transactions')
    borrower = relationship('Borrower', back_populates='transactions')
