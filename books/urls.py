from django.urls import path
from . import views


app_name = "books"
urlpatterns = [
    path("create/", views.BookCreate.as_view()),
    path("books/", views.BookReview.as_view()),
    path("update/<int:pk>/", views.BookUpdate.as_view()),
    path("delete/<int:pk>/", views.BookDelete.as_view()),
]