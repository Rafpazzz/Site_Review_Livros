from django.shortcuts import render
from .models import Books
# Create your views here.

def add_book(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano_publicacao = request.POST.get('ano_publicacao')
        resumo = request.POST.get('resumo')

        book = Books(titulo=titulo, autor=autor, editora=editora, ano_publicacao=ano_publicacao, resumo=resumo)
        book.save()

        return render(request, 'success.html')
    
    return render(request, 'add_book.html')


def all_books(request):
    books = Books.objects.all()
    return render(request, 'all_books.html', {'books': books})