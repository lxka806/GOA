from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_phones, name="all_phones"),
    path("detail/<int:id>/", views.phone_details, name="phone_details"),
    path("delete/<int:id>/", views.delete_phone, name="delete_phone"),
]