from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.base import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, unique=True)
    books = relationship('Book', back_populates='author')
