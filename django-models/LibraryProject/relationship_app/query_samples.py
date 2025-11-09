import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_name):
    """
    Query all books by a specific author.
    
    Args:
        author_name (str): The name of the author
    
    Returns:
        QuerySet: All books written by the author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        
        print(f"\n=== Books by {author_name} ===")
        if books.exists():
            for book in books:
                print(f"- {book.title}")
        else:
            print("No books found for this author.")
        
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")
        return Book.objects.none()


def list_books_in_library(library_name):
    """
    List all books in a library.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        QuerySet: All books in the library
    """
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        
        print(f"\n=== Books in {library_name} ===")
        if books.exists():
            for book in books:
                print(f"- {book.title} by {book.author.name}")
        else:
            print("No books found in this library.")
        
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return Book.objects.none()


def retrieve_librarian_for_library(library_name):
    """
    Retrieve the librarian for a library.
    
    Args:
        library_name (str): The name of the library
    
    Returns:
        Librarian: The librarian object for the library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        
        print(f"\n=== Librarian for {library_name} ===")
        print(f"Librarian: {librarian.name}")
        
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")
        return None


# Example usage with sample data
if __name__ == "__main__":
    print("Django ORM Relationship Queries Demo")
    print("=" * 50)
    
    # Create sample data (if needed)
    print("\n--- Creating Sample Data ---")
    
    # Create authors
    author1, _ = Author.objects.get_or_create(name="J.K. Rowling")
    author2, _ = Author.objects.get_or_create(name="George Orwell")
    
    # Create books
    book1, _ = Book.objects.get_or_create(
        title="Harry Potter and the Philosopher's Stone",
        author=author1
    )
    book2, _ = Book.objects.get_or_create(
        title="Harry Potter and the Chamber of Secrets",
        author=author1
    )
    book3, _ = Book.objects.get_or_create(
        title="1984",
        author=author2
    )
    book4, _ = Book.objects.get_or_create(
        title="Animal Farm",
        author=author2
    )
    
    # Create library
    library1, _ = Library.objects.get_or_create(name="Central Library")
    library1.books.add(book1, book2, book3)
    
    library2, _ = Library.objects.get_or_create(name="City Library")
    library2.books.add(book3, book4)
    
    # Create librarians
    librarian1, _ = Librarian.objects.get_or_create(
        name="Alice Johnson",
        library=library1
    )
    librarian2, _ = Librarian.objects.get_or_create(
        name="Bob Smith",
        library=library2
    )
    
    print("Sample data created successfully!")
    
    # Run sample queries
    print("\n" + "=" * 50)
    print("RUNNING SAMPLE QUERIES")
    print("=" * 50)
    
    # Query 1: Query all books by a specific author
    query_books_by_author("J.K. Rowling")
    query_books_by_author("George Orwell")
    
    # Query 2: List all books in a library
    list_books_in_library("Central Library")
    list_books_in_library("City Library")
    
    # Query 3: Retrieve the librarian for a library
    retrieve_librarian_for_library("Central Library")
    retrieve_librarian_for_library("City Library")