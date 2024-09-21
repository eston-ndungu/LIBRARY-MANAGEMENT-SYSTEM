from cli_mthods import add_author, view_authors, add_book, view_books

# CLI Menu
def menu():
    print("\n Welcome to Library Management System. What would you like to do today?")
    print("1. View Books")
    print("2. View Authors")
    print("3. Add Book")
    print("4. Add Author")
    print("0. Exit")

# Main function to control menu flow
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
            add_author()
        elif choice == "0":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
