# Utils Folder Documentation

## Overview
A simple **Book Management System** with an interactive command-line interface. This application allows users to add, list, mark as read, and delete books from their personal collection.

---

## Architecture

### Two-Module Design

```
utils/
├── app.py          # User Interface Layer (CLI menu system)
└── database.py     # Data Layer (Book storage and operations)
```

---

## Module Breakdown

### `database.py` - Data Layer

Handles all data persistence and book operations.

**Global State:**
- `books`: List that stores all book dictionaries

**Functions:**

| Function | Parameters | Returns | Purpose |
|----------|-----------|---------|---------|
| `add_book(name, author)` | `name: str`<br>`author: str` | None | Adds a new book to the collection with `read=False` |
| `get_all_books()` | None | `list[dict]` | Returns all books in the collection |
| `mark_book_read(name)` | `name: str` | None | Marks a book as read by matching its name |
| `delete_book(name)` | `name: str` | None | Removes a book from the collection by name |

**Book Data Structure:**
```python
{
    "name": str,      # Book title
    "author": str,    # Book author
    "read": bool      # Reading status (False = unread, True = read)
}
```

---

### `app.py` - User Interface Layer

Provides an interactive menu-driven interface for managing books.

**Menu Commands:**

| Command | Function | Action |
|---------|----------|--------|
| `a` | `prompt_add_book()` | Add a new book |
| `l` | `list_book()` | List all books with read status |
| `r` | `prompt_read_book()` | Mark a book as read |
| `d` | `prompt_delete_book()` | Delete a book |
| `q` | Exit | Quit the application |

**Functions:**

- **`menu()`** 
  - Main event loop that displays menu and processes user input
  - Continues until user enters 'q'

- **`prompt_add_book()`** 
  - Prompts user for book name and author
  - Calls `database.add_book()` to store the book

- **`list_book()`** 
  - Retrieves all books from database
  - Displays each book with formatted read status (YES/NO)

- **`prompt_read_book()`** 
  - Prompts user for book name
  - Calls `database.mark_book_read()` to update status

- **`prompt_delete_book()`** 
  - Prompts user for book name
  - Calls `database.delete_book()` to remove the book

---

## Usage Example

```
Enter:
-- 'a' to add a new book
-- 'l' to list all books
-- 'r' to mark a book as read
-- 'd' to delete a book
-- 'q' to quit

Your choice: a
Enter book name: 1984
Enter book author: George Orwell

Your choice: l
1984 by George Orwell, read: NO

Your choice: r
Enter the name of the book you finished reading: 1984

Your choice: l
1984 by George Orwell, read: YES

Your choice: q
```

---

## Key Features

✅ Add books with name and author  
✅ View all books in collection  
✅ Track reading status for each book  
✅ Delete books from collection  
✅ Simple command-line interface  
✅ Input validation with error messages  

---

## Data Persistence Note

⚠️ **Current Limitation:** Books are stored in memory only. Data is lost when the program exits. For persistent storage, consider:
- Adding file I/O (JSON/CSV)
- Integrating a database (SQLite, PostgreSQL)

---

## How to Run

```bash
python utils/app.py
```

---

## Requirements

- Python 3.6+
- No external dependencies
