from django import forms
from django.forms import fields
from book.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'