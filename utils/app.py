from utils import database

USER_CHOICE = """
Enter:
-- 'a' to add a new book
-- 'l' to list all books
-- 'r' to mark a book as read
-- 'd' to delete a book
-- 'q' to quit

Your choice:"""

def menu():
    user_choice = input(USER_CHOICE)
    while user_choice != 'q':
        if user_choice == 'a':
            prompt_add_book()
        elif user_choice == 'l':
            list_book()
        elif user_choice == 'r':
            prompt_read_book()
        elif user_choice == 'd':
            prompt_delete_book()
        else:
            print('Unknown command.Please try again.')

        user_choice = input(USER_CHOICE)


# def prompt_add_book() ask for book name and author
def prompt_add_book():
    name = input('Enter book name: ')
    author = input('Enter book author: ')

    database.add_book(name, author)

#def list_book() show all the books in our list
def list_book():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


#def prompt_read_book() ask for book name and change it to "read" in our list
def prompt_read_book():
    name = input('Enter the name of the book you finished reading: ')

    database.mark_book_read(name)


#def prompt_delete_book() ask  for book name and remove book from list
def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')


menu()


