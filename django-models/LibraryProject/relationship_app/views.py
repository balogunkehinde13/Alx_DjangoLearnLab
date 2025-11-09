from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Book, Library
from .forms import BookForm


def list_books(request):
    """
    Function-based view that lists all books in the database.
    
    This view retrieves all books and renders them in a template
    showing the book title and author name.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """
    Class-based view that displays details for a specific library.
    
    This view shows the library name and all books available in that library
    along with their authors.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Authentication Views

def register(request):
    """
    View for user registration.
    
    Handles GET and POST requests for user registration.
    On successful registration, logs the user in and redirects to the books list.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, f'Account created successfully! Welcome, {user.username}!')
            return redirect('list_books')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})


def user_login(request):
    """
    View for user login.
    
    Handles GET and POST requests for user authentication.
    On successful login, redirects to the books list.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('list_books')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'relationship_app/login.html', {'form': form})


def user_logout(request):
    """
    View for user logout.
    
    Logs out the current user and displays a logout confirmation page.
    """
    logout(request)
    messages.info(request, 'You have been successfully logged out.')
    return render(request, 'relationship_app/logout.html')


# Role-Based Access Control Helper Functions

def is_admin(user):
    """Check if user has Admin role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    """Check if user has Librarian role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    """Check if user has Member role."""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Role-Based Views

@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    """
    Admin-only view.
    
    This view is accessible only to users with the 'Admin' role.
    Displays administrative functions and statistics.
    """
    context = {
        'role': 'Admin',
        'user': request.user,
    }
    return render(request, 'relationship_app/admin_view.html', context)


@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    """
    Librarian-only view.
    
    This view is accessible only to users with the 'Librarian' role.
    Displays library management functions.
    """
    context = {
        'role': 'Librarian',
        'user': request.user,
    }
    return render(request, 'relationship_app/librarian_view.html', context)


@user_passes_test(is_member, login_url='login')
def member_view(request):
    """
    Member-only view.
    
    This view is accessible only to users with the 'Member' role.
    Displays member-specific content and book browsing features.
    """
    context = {
        'role': 'Member',
        'user': request.user,
    }
    return render(request, 'relationship_app/member_view.html', context)


# Permission-Based CRUD Views for Books

@permission_required('relationship_app.can_add_book', login_url='login', raise_exception=True)
def add_book(request):
    """
    View for adding a new book.
    
    Requires 'can_add_book' permission.
    Only users with this permission can create new books.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was successfully added!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    
    context = {
        'form': form,
        'action': 'Add',
    }
    return render(request, 'relationship_app/book_form.html', context)


@permission_required('relationship_app.can_change_book', login_url='login', raise_exception=True)
def edit_book(request, pk):
    """
    View for editing an existing book.
    
    Requires 'can_change_book' permission.
    Only users with this permission can modify book details.
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was successfully updated!')
            return redirect('list_books')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'action': 'Edit',
        'book': book,
    }
    return render(request, 'relationship_app/book_form.html', context)


@permission_required('relationship_app.can_delete_book', login_url='login', raise_exception=True)
def delete_book(request, pk):
    """
    View for deleting a book.
    
    Requires 'can_delete_book' permission.
    Only users with this permission can delete books from the system.
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" was successfully deleted!')
        return redirect('list_books')
    
    context = {
        'book': book,
    }
    return render(request, 'relationship_app/book_confirm_delete.html', context)