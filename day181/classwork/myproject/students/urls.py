from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_students),
    path('<int:id>/', views.student_with_id),
]