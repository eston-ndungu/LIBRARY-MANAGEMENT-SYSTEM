from cli_methods import view_authors, view_books, add_book, view_borrowers, checkout_book, view_transactions, return_book

def menu():
    print("\nWelcome to the Library Management System. What would you like to do today?")
    print("1. View Books")
    print("2. View Authors")
    print("3. Add Book")
    print("4. View Borrowers")
    print("5. View Transactions")
    print("6. Checkout Book")
    print("7. Return Book")
    print("0. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            view_books()
        elif choice == "2":
            view_authors()
        elif choice == "3":
            add_book()
        elif choice == "4":
            view_borrowers()
        elif choice == "5":
            view_transactions()
        elif choice == "6":
            checkout_book()
        elif choice == "7":
            return_book()
        elif choice == "0":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
