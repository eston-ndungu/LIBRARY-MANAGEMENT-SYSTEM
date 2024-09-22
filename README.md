# LIBRARY-MANAGEMENT-SYSTEM

## Overview

This Library Management System (LMS) is built using Python and SQLAlchemy, allowing for the management of books, authors, borrowers, and transactions within a library. 

The application supports functionalities such as adding books, viewing authors, checking out books, and returning them.

## Features

- View Authors: List all authors in the database.

- Add Book: Add new books to the system, associating them with existing or new authors.

- View Books: Display a list of all books along with their authors and availability status.

- View Borrowers: Show all borrowers and the books they currently have checked out.

- View Transactions: List all book transactions, including checkout and return dates.

- Checkout Book: Allow borrowers to check out available books.

- Return Book: Facilitate the return of books, updating their availability.

# Installation
- Run pipenv install to run dependecies

- Run pipenv install sqlachemy 

- Run pipenv install tabulate

- Run pipenv shell to create a virtual environment for the project.

# Code Structure

- models/: Contains the SQLAlchemy models for Authors, Books, Borrowers, and Transactions.

- cli_methods.py: Defines functions for various command-line operations.

- config.py: Sets up the database connection.

- cli.py: The main entry point for the application, containing the menu and user interactions.

# Database Schema
The application uses four main tables:

## Authors: 
Stores information about authors.

- id: Unique identifier for the author.

- name: Name of the author.

## Books:
 Contains book details.

- id: Unique identifier for the book.

- title: Title of the book.

- availability_status: Indicates if the book is currently available.

- author_id: Foreign key referencing the authors table.

## Borrowers: 

Represents individuals borrowing books.

- id: Unique identifier for the borrower.

- name: Name of the borrower.

## Transactions: 
Records the borrowing activity.

- id: Unique identifier for the transaction.

- book_id: Foreign key referencing the books table.

- borrower_id: Foreign key referencing the borrowers table.

- checkout_date: Date when the book was borrowed.

- return_date: Date when the book was returned (nullable).

# Instructions for use
 Fork the repo
- click watch to watch for updates

- clone the forked repo for test purposes

# Contribution

 This project is still under development, and you can use it for learning and improving yourself.

# Running the Application

To run the project in CLI  execute the following command in your virtual enviroment; python cli.py

# Watch Video Below

https://drive.google.com/file/d/1iQV9z-sy6I5Cc8xiFhfN2UHKGQ_MpvRb/view


# Licence

- MIT

# Author

- Eston Ndungu


