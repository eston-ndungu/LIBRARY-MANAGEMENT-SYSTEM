from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from models.base import Base
from sqlalchemy.orm import relationship

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    is_available = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    author = relationship('Author', back_populates='books')
