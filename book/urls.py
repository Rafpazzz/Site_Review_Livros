from django.urls import path
from . import views

urlpatterns = [
    path('add_book', views.add_book, name='add_book'),
    path('success', views.add_book, name='success'),
    path('all_books', views.all_books, name='all_books'),
]