from sqlalchemy import Column, String, Integer
from models.base import Base
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    books = relationship('Book', back_populates='author')
