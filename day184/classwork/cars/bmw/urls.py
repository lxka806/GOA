from django.urls import path
from . import views

urlpatterns = [
    path("", views.cars_list, name="cars_list"),
    path("<int:id>/", views.car_details, name="car_details"),
    path("delete/<int:id>/", views.delete_car, name="delete_car"),
]