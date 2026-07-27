from django.urls import path
from . import views

urlpatterns = [
    path("", views.add_task, name="main"),
    path("delete/<int:id>/", views.delete, name="delete"),
]