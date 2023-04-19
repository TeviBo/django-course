from django.urls import path

from . import views

APP_NAME = "users_app"

urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("api/login/", views.GoogleLoginView.as_view(), name="users-google_login"),
]
