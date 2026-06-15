from django.urls import path
from . import views

urlpatterns = {
    path('', views.bmw),
    path('e39', views.bmw_e39),
    path('m3', views.bmw_m3),
    path('m8', views.bmw_m8),
}
