from django.db import models
from book.models import Books
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="reviews")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()

    RATING_CHOICES = [
        (1, "⭐"),
        (2, "⭐⭐"),
        (3, "⭐⭐⭐"),
        (4, "⭐⭐⭐⭐"),
        (5, "⭐⭐⭐⭐⭐"),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Nota")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.titulo} - {self.author.username}"
