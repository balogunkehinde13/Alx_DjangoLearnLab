## 2. RETRIEVE Operation

| Command | Output | Notes |
| :--- | :--- | :--- |
| `retrieved_book = Book.objects.get(pk=1)` | *No output* | Retrieves the object by its primary key (ID). |
| `print(f"Title: {retrieved_book.title}, Author: {retrieved_book.author}, Year: {retrieved_book.publication_year}")` | `Title: 1984, Author: George Orwell, Year: 1949` | Displays all attributes for verification. |