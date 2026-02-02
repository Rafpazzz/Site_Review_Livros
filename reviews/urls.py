from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:book_id>/', views.add_review, name='add_review'),
    path('view_review/<int:review_id>/', views.view_review, name='view_review'),
]