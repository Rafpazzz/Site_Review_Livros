from django.urls import path
from . import views

urlpatterns = [
    path('all_books', views.all_books, name='all_books'),
    path('search_book', views.search_book, name='search_book'),
    path('<int:id>', views.detalhes, name='detalhes'),
]