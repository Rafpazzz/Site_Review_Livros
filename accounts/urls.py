from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset_form/', views.password_reset_form, name='password_reset_form'),
    path('perfil/', views.perfil, name='perfil'),
    path('configuracao/', views.system_config_home, name='admin_config_home'),
    path('configuracao/livros/', views.manage_books, name='admin_books'),
    path('configuracao/usuarios/', views.manage_users, name='admin_users'),
    path('configuracao/usuarios/exportar/csv/', views.export_users_csv, name='admin_users_export_csv'),
    path('configuracao/usuarios/exportar/pdf/', views.export_users_pdf, name='admin_users_export_pdf'),
    path('configuracao/laboratorio/', views.manage_lab, name='admin_lab'),
]
