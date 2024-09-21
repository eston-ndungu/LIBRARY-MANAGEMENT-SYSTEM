from models.author import Author
from models.book import Book
from config import get_session

session = get_session()

# Add authors
authors = [
    Author(name="George Orwell"),
    Author(name="J.K. Rowling"),
    Author(name="J.R.R. Tolkien")
]

session.add_all(authors)
session.commit()

# Add books
books = [
    Book(title="1984", author=authors[0]),
    Book(title="Animal Farm", author=authors[0]),
    Book(title="Harry Potter and the Sorcerer's Stone", author=authors[1]),
    Book(title="The Hobbit", author=authors[2])
]

session.add_all(books)
session.commit()

print("Data populated successfully.")
