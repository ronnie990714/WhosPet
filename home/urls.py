from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('gps/', views.gps, name='gps'),
    path('facility/', views.facility, name='facility'),
    path('info/', views.info, name='info'),
    path('accounts/',include('allauth.urls'))
]