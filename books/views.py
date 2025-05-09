from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import View
from django.shortcuts import render

from books.forms import Book_Form
from books.models import Book

class Book_View(View):
	initial = {"key": "value"} # Utiliza los valores por default dentro de las definiciones del modelo
	form_class = Book_Form # Por si quiero un formulario (se comenta esta linea si no quiero un formulario)
	template_name = "books/api.html" # Quien va a ser el render de nuestros resultados

	def get(self, request, *args, **kwargs):
		isbn = self.kwargs["isbn"] # Preguntamos si en las keywords viene el isbn
		try:
			book = Book.objects.get(id=isbn) # intentamos pedir a la base de datos y si lo encuentra lo guarda
			form = self.form_class(instance=book)
		except Book.DoesNotExist:
			form = self.form_class(initial=self.initial)
			isbn = 0
		return render(request, self.template_name, {"form": form, "isbn":isbn})


	def post(self, request, *args, **kwargs):
		if "cancel_page_button" in request.POST:
			return HttpResponseRedirect("/")
		if "save_page_button" in request.POST:
			isbn = self.kwargs["isbn"]

			try:
				instance=Book.objects.get(id=isbn)
				form = self.form_class(request.POST or None, instance=instance) # Este metodo ahorra mucho tiempo
			except Book.DoesNotExist:
				form = self.form_class(request.POST)
			if form.is_valid():
				book = form.save() # Automaticamente el sistema le crea un identificador (isbn)

				return render(request, "books/book-save.html", {"book": book}) # Renderear que salvamos la informacion
		return HttpResponseRedirect("/")

	def dispatch(self, *args, **kwargs):
		return super(Book_View, self).dispatch(*args, **kwargs)



class Api_View(View):
	form_class = Book_Form
	template_name = "api/api.html"

	def get(self, request, *args, **kwargs):
		isbn = self.kwargs["isbn"]
		try:
			book = Book.objects.get(id=isbn)
			form = self.form_class(instance=book)
		except Book.DoesNotExist:
			form = self.form_class(initial=self.initial)
			#paciente_count = Paciente.objects.filter().count()
			isbn = 0 # request.user.username +"-"+ str(pacient_count)
		return render(request, self.template_name, {"form":form, "isbn":isbn}) # nos muestra el formulario para llenar

	###@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Api_View, self).dispatch(*args, **kwargs)
