from django.urls import path, re_path
from books.views import Book_View

urlpatterns = [
   re_path(r"^(?P<isbn>[^/]+)/api/$", Book_View.as_view()),
]
