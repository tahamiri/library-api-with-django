from django.urls import path
from . import views




app_name = "accounts"
urlpatterns = [
    path("register/", views.UserRegister.as_view()),
    path("users/", views.UserReview.as_view()),
    path("update/<int:pk>/", views.UserUpdate.as_view()),
    path("delete/<int:pk>/", views.UserDelete.as_view()),
]
