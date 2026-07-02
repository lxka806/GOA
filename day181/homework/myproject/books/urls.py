from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
]