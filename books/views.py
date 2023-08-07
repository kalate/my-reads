from django.shortcuts import render
from django.views import generic

from .models import Book


class IndexView(generic.ListView):
    model = Book
    template_name = "books/index.html"


class DetailView(generic.DetailView):
    model = Book
    template_name = "books/detail.html"