from django.urls import path
from .views import get_tasks, update_task

urlpatterns = [
    path("tasks/", get_tasks, name="get_tasks"),
    path("tasks/<int:task_id>/", update_task, name="update_task"),
]