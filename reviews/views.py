from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from book.models import Books
from .forms import ReviewForm

# Create your views here.
@login_required
def add_review(request, book_id):
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
