from django.db import models
from django_countries.fields import CountryField

class Book(models.Model):
	GENRE_CHOICES = (
		("1", "Terror"),
		("2", "Fantasia"),
		("3", "Novela"),
	)

	author = models.CharField(max_length=128)
	date = models.DateField()
	genre = models.CharField(max_length=16, choices=GENRE_CHOICES)
	genre_other = models.CharField(max_length=32, blank=True, null=True) # blank es que puede ir vacio y null es que siempre debe de estar en todos los formularios que yo haga
	country = CountryField()
