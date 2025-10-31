## 3. UPDATE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `book_to_update = Book.objects.get(title="1984")` | *No output* | Retrieves the book again. |
| `book_to_update.title = "Nineteen Eighty-Four"` | *No output* | Modifies the title attribute. |
| `book_to_update.save()` | *No output* | Saves the change to the database. |
| `book_to_update` | `<Book: Nineteen Eighty-Four by George Orwell (1949)>` | Displays the book with the **updated title**. |
