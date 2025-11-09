# 📝 File: `CRUD_operations.md`

This document details the commands and outputs from the Django shell session demonstrating the CRUD operations for the `bookshelf.Book` model.

The sequence is executed after successfully running `python manage.py shell`.

---

## 1. CREATE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `from bookshelf.models import Book` | *No output* | Imports the model. |
| `book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)` | `<Book: 1984 by George Orwell (1949)>` | Creates the book instance. |
| `book.pk` | `1` | Verifies the book has an ID. |

---

## 2. RETRIEVE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `retrieved_book = Book.objects.get(pk=1)` | *No output* | Retrieves the object by its primary key (ID). |
| `print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")` | `Title: 1984, Author: George Orwell, Year: 1949` | Displays all attributes for verification. |

---

## 3. UPDATE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `book_to_update = Book.objects.get(title="1984")` | *No output* | Retrieves the book again. |
| `book_to_update.title = "Nineteen Eighty-Four"` | *No output* | Modifies the title attribute. |
| `book_to_update.save()` | *No output* | Saves the change to the database. |
| `book_to_update` | `<Book: Nineteen Eighty-Four by George Orwell (1949)>` | Displays the book with the **updated title**. |

---

## 4. DELETE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `book_to_delete = Book.objects.get(author="George Orwell")` | *No output* | Retrieves the book before deletion. |
| `book_to_delete.delete()` | `(1, {'bookshelf.Book': 1})` | Deletes the instance and returns the number of objects deleted. |
| `Book.objects.all()` | `<QuerySet []>` | Confirms the deletion by showing an **empty queryset**. |