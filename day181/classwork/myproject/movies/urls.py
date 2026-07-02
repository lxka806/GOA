from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies),
    path('<int:id>/', views.movie_id)
]