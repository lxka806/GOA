from django.urls import path
from . import views

urlpatterns = [
    path('', views.All_laptop),
    path('dell/', views.Dell),
    path('hp/', views.Hp),
    path('lenovo/', views.Lenovo),
    path('asus/', views.Asus),
    path('apple/', views.Apple),
]