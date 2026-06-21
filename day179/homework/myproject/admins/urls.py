from django.urls import path
from . import views

urlpatterns = [
    path('', views.All_Admin),
    path('<int:id>/', views.Admin)
]