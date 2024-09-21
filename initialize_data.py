from models.author import Author
from models.book import Book
from models.borrower import Borrower
from models.transaction import Transaction
from config import get_session
from datetime import date

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

# Add borrowers
borrowers = [
    Borrower(name="Alice Johnson"),
    Borrower(name="Bob Smith"),
    Borrower(name="Charlie Davis")
]

session.add_all(borrowers)
session.commit()

# Add transactions (borrow books)
transactions = [
    Transaction(book=books[0], borrower=borrowers[0], checkout_date=date(2024, 9, 1)),
    Transaction(book=books[1], borrower=borrowers[1], checkout_date=date(2024, 9, 5)),
    Transaction(book=books[2], borrower=borrowers[2], checkout_date=date(2024, 9, 10)),
    Transaction(book=books[3], borrower=borrowers[0], checkout_date=date(2024, 9, 15))
]

session.add_all(transactions)
session.commit()

print("Data populated successfully.")
