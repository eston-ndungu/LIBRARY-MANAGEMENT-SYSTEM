from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base import Base

class Borrower(Base):
    __tablename__ = 'borrowers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    transactions = relationship('Transaction', back_populates='borrower')
