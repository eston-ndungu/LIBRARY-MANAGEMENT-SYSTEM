from models.author import Author
from models.book import Book
from models.borrower import Borrower
from models.transaction import Transaction
from config import get_session
from tabulate import tabulate
from datetime import date

session = get_session()

# View Authors
def view_authors():
    authors = session.query(Author).all()
    rows = [[author.id, author.name] for author in authors]
    print(tabulate(rows, headers=["ID", "Name"], tablefmt="pretty"))

# Add Book
def add_book():
    title = input("Enter book title: ")
    author_name = input("Enter author name: ")

    existing_book = session.query(Book).filter_by(title=title).first()

    if existing_book:
        print(f"Book '{title}' already exists.")
        return

    author = session.query(Author).filter_by(name=author_name).first()

    if author:
        book = Book(title=title, author=author)
    else:
        author = Author(name=author_name)
        session.add(author)
        session.commit()
        book = Book(title=title, author=author)

    session.add(book)
    session.commit()
    print(f"Book '{title}' added successfully under author '{author_name}'.")

# View Books
def view_books():
    books = session.query(Book).all()
    rows = [[book.id, book.title, book.author.name, book.availability_status] for book in books]
    print(tabulate(rows, headers=["ID", "Title", "Author", "Availability"], tablefmt="pretty"))

def view_borrowers():
    borrowers = session.query(Borrower).all()
    
    borrower_data = []
    for borrower in borrowers:
        borrowed_books = [transaction.book.title for transaction in borrower.transactions if transaction.return_date is None]
        books_list = ', '.join(borrowed_books) if borrowed_books else 'No books borrowed'
        
        borrower_data.append([borrower.id, borrower.name, books_list])
    
    print(tabulate(borrower_data, headers=["ID", "Name", "Borrowed Books"], tablefmt="pretty"))

# View Transactions
def view_transactions():
    transactions = session.query(Transaction).all()
    if not transactions:
        print("No transactions found.")
        return
    
    transaction_data = []
    for transaction in transactions:
        transaction_data.append([
            transaction.book.title,
            transaction.borrower.name,
            transaction.checkout_date,
            transaction.return_date if transaction.return_date else "Not Returned"
        ])
    
    print(tabulate(transaction_data, headers=["Book Title", "Borrower Name", "Checkout Date", "Return Date"], tablefmt="pretty"))

def checkout_book():
    book_title = input("Enter the title of the book to checkout: ")
    borrower_name = input("Enter your name: ").strip()  # Remove any leading/trailing whitespace
    
    # Check if the book exists
    book = session.query(Book).filter_by(title=book_title).first()
    if not book:
        print(f"Book '{book_title}' does not exist.")
        return
    
    # Check if the book is currently borrowed
    active_transaction = session.query(Transaction).filter_by(book_id=book.id, return_date=None).first()
    if active_transaction:
        print(f"Book '{book_title}' is currently borrowed. Please wait until its returned.")
        return

    # Check if the borrower exists (case insensitive)
    borrower = session.query(Borrower).filter(Borrower.name.ilike(borrower_name)).first()

    # If the borrower doesn't exist, prompt to add them
    if not borrower:
        add_borrower = input(f"Borrower '{borrower_name}' does not exist. Would you like to add them? (y/n): ")
        if add_borrower.lower() == 'y':
            borrower = Borrower(name=borrower_name)
            session.add(borrower)
            session.commit()  # Ensure the borrower is committed to the database
            print(f"Borrower '{borrower_name}' added successfully.")
        else:
            print("Checkout cancelled.")
            return

    # Proceed with the checkout
    transaction = Transaction(book=book, borrower=borrower, checkout_date=date.today())
    book.availability_status = False  # Mark the book as checked out
    session.add(transaction)
    session.commit()
    print(f"Book '{book_title}' checked out successfully by '{borrower_name}'.")

def return_book():
    book_title = input("Enter the title of the book to return: ")
    borrower_name = input("Enter your name: ").strip()  # Remove any leading/trailing whitespace
    
    # Check if the book exists
    book = session.query(Book).filter_by(title=book_title).first()
    if not book:
        print(f"Book '{book_title}' does not exist.")
        return

    # Check if the borrower exists
    borrower = session.query(Borrower).filter(Borrower.name.ilike(borrower_name)).first()
    if not borrower:
        print(f"Borrower '{borrower_name}' does not exist.")
        return

    # Check if there is an active transaction for the borrower and the book
    transaction = session.query(Transaction).filter_by(book_id=book.id, borrower_id=borrower.id, return_date=None).first()
    
    if not transaction:
        print(f"No active transaction found for '{borrower_name}' with the book '{book_title}'.")
        return
    
    # Set the return date to today
    transaction.return_date = date.today()
    book.availability_status = True  # Mark the book as available again
    
    session.commit()  # Save changes to the database
    print(f"Book '{book_title}' returned successfully by '{borrower_name}'.")

