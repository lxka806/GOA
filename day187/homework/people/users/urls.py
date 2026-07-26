from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_user, name="main_users"),
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("profile/", views.user_profile, name="user_profile"),
    path("logout/", views.logout_user, name="logout_user"),
    path("edit/", views.edit_user, name="edit_user")
]