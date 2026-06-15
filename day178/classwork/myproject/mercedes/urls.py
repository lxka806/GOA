from django.urls import path
from . import views

urlpatterns = {
    path('', views.mercedes),
    path('e39', views.mercedes_e39),
    path('m3', views.mercedes_m3),
    path('m8', views.mercedes_m8),
}
