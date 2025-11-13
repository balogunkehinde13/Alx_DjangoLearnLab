from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_protect
from advanced_features_and_security.LibraryProject.bookshelf.forms import ExampleForm
from .models import Book

@permission_required('myapp.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

@permission_required('myapp.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Book.objects.create(title=title, content=content, author=request.user)
        return redirect('book_list')
    return render(request, 'myapp/create_book.html')

@permission_required('myapp.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.content = request.POST.get('content')
        book.save()
        return redirect('book_list')
    return render(request, 'myapp/edit_book.html', {'book': book})

@permission_required('myapp.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

@csrf_protect
def example_form_view(request):
    """
    Displays and processes ExampleForm securely.
    Uses CSRF protection and Django’s ORM for safe database operations.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})