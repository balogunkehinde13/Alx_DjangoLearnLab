### Delete Operation

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.get(author="George Orwell")
book.delete()
Book.objects.all()
```

**Output**
```python
# (1, {'bookshelf.Book': 1}) # Output from book_to_delete.delete()
# <QuerySet []> # Output from Book.objects.all() confirming deletion
```