from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('password_reset_form', views.password_reset_form, name='password_reset_form'),
]