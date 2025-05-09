from django.forms import ModelForm
from books.models import Book

class Book_Form(ModelForm):
	class Meta:
		model = Book
		fields = ["author", "date", "genre", "country"]
