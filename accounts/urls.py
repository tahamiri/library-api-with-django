from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



app_name = "accounts"
urlpatterns = [
    path("register/", views.UserRegister.as_view()),
    path("users/", views.UserReview.as_view()),
    path("update/<int:pk>/", views.UserUpdate.as_view()),
    path("delete/<int:pk>/", views.UserDelete.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
