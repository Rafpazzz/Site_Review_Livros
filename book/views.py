from django.shortcuts import render, get_object_or_404
from .models import Books
from django.contrib.auth.decorators import login_required
# Create your views here.

def all_books(request):
    books = Books.objects.all()
    return render(request, 'all_books.html', {'books': books})

@login_required
def search_book(request):
    query = request.GET.get('q')
    if query:
        books = Books.objects.filter(titulo__icontains=query)
    else:
        books = Books.objects.none()
    return render(request, 'search_book.html', {'books': books, 'query': query})

@login_required
def detalhes(request, id):
    book = get_object_or_404(Books, pk=id)
    return render(request, 'detalhes.html', {'book': book})