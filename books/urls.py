from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    # ex: /books/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /books/4
    path("<int:pk>/", views.DetailView.as_view(), name="detail")
]