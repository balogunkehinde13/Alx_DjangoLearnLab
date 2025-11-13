## 1. CREATE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `from bookshelf.models import Book` | *No output* | Imports the model. |
| `book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)` | `<Book: 1984 by George Orwell (1949)>` | Creates the book instance. |
| `book.pk` | `1` | Verifies the book has an ID. |