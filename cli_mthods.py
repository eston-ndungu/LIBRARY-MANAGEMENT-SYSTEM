from models.author import Author
from models.book import Book
from config import get_session
from tabulate import tabulate

session = get_session()

# Adding Author
def add_author():
    name = input("Enter author name: ")
    author = Author(name=name)
    session.add(author)
    session.commit()
    print(f"Author '{name}' added successfully.")

# Viewing Authors
def view_authors():
    authors = session.query(Author).all()
    rows = [[author.id, author.name] for author in authors]
    table = tabulate(rows, headers=["ID", "Name"], tablefmt="pretty")
    print(table)

# Adding Book
def add_book():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")
    author = session.query(Author).filter_by(name=author_name).first()
    if author:
        book = Book(title=title, author=author)
        session.add(book)
        session.commit()
        print(f"Book '{title}' added successfully.")
    else:
        print("Author not found.")

# Viewing Books
def view_books():
    books = session.query(Book).all()
    rows = [[book.id, book.title, book.author.name, book.availability_status] for book in books]
    table = tabulate(rows, headers=["ID", "Title", "Author", "Availability"], tablefmt="pretty")
    print(table)
