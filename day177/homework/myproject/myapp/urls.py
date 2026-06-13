from django.urls import path
from . import views

urlpatterns = [
    path('', views.users),
    path('delete/', views.user_delete),
    path('add/', views.user_add),
    path('update/', views.user_update)
]