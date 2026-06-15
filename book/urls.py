from django.urls import path
from . import views

urlpatterns = [
    path('all_books', views.all_books, name='all_books'),
    path('search_book', views.search_book, name='search_book'),
    path('exportar/csv/', views.export_books_csv, name='admin_books_export_csv'),
    path('exportar/pdf/', views.export_books_pdf, name='admin_books_export_pdf'),
    path('<int:id>', views.detalhes, name='detalhes'),
]
