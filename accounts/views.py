from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .admin import CustomUserCreationForm
from django.contrib import messages
from reviews.models import Review

# Create your views here.

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':    
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('all_books')

        else:
            print(form.errors)
    
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('all_books')
        else:
            messages.error(request, 'Invalid email or password')
            
    return render(request, 'registration/login.html')


def password_reset_form(request):
    return render(request, 'registration/password_reset_form.html')

@login_required
def perfil(request):
    user_reviews = Review.objects.filter(autor=request.user).order_by('-created_at')

    return render(request, 'registration/perfil.html', {'reviews': user_reviews})