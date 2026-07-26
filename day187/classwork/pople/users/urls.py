from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_users, name="main_user"),
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
]