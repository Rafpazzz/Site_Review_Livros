from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from book.models import Books
from .forms import ReviewForm
from .models import Review

# Create your views here.
def add_review(request, book_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    book = get_object_or_404(Books, pk=book_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.autor = request.user
            review.save()
           
            return redirect('detalhes', id=book_id)
    else:

        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'book': book})



def view_review(request, review_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'view_review.html', {'review' : review})


def delete_review(request, review_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    review = get_object_or_404(Review, pk=review_id)
    
    if request.user != review.autor:
        messages.error(request, "Você não tem permissão para excluir esta avaliação.")
        return redirect('view_review', review_id=review.id)
    
    review.delete()
    
    messages.success(request, "Avaliação excluída com sucesso!")
    return redirect('perfil') 



def editar_review(request, review_id):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    review = get_object_or_404(Review, pk=review_id)
    
    if request.user != review.autor:
        messages.error(request, "Você não tem permissão para excluir esta avaliação.")
        return redirect('view_review', review_id=review.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Sua avaliação foi atualizada com sucesso")
            return redirect('view_review', review_id=review.id)
    else:
         form = ReviewForm(instance=review)
    
    return render(request, 'add_review.html', {
        'form': form, 
        'book': review.book 
    })
    
def list_review(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Voce precisa esta logado para fazer essa ação")
        return redirect('login')
    
    review_list = Review.objects.all().order_by('id')
    paginator = Paginator(review_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list_review.html', {'page_obj' : page_obj})