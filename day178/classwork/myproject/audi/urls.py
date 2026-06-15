from django.urls import path
from . import views

urlpatterns = {
    path('', views.audi),
    path('e39', views.audi_e39),
    path('m3', views.audi_m3),
    path('m8', views.audi_m8),
}
