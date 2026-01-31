from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text'] # <--- Nome novo aqui

        widgets = {
            # A chave aqui TAMBÉM tem que ser o nome novo:
            'review_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), 
            'rating': forms.Select(attrs={'class': 'form-control'})
        }
