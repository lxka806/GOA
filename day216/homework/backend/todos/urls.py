from django.urls import path
from .views import current_user, csrf_token, get_tasks, log_in, log_out, register, update_task

urlpatterns = [
    path("auth/csrf/", csrf_token, name="csrf_token"),
    path("auth/user/", current_user, name="current_user"),
    path("auth/register/", register, name="register"),
    path("auth/login/", log_in, name="login"),
    path("auth/logout/", log_out, name="logout"),
    path("tasks/", get_tasks, name="get_tasks"),
    path("tasks/<int:task_id>/", update_task, name="update_task"),
]