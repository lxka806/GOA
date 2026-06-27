from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cars),
    path('<int:id>/', views.car_with_id)
]