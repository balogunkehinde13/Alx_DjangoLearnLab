## 4. DELETE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `book_to_delete = Book.objects.get(author="George Orwell")` | *No output* | Retrieves the book before deletion. |
| `book_to_delete.delete()` | `(1, {'bookshelf.Book': 1})` | Deletes the instance and returns the number of objects deleted. |
| `Book.objects.all()` | `<QuerySet []>` | Confirms the deletion by showing an **empty queryset**. |