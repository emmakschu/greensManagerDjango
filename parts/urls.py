from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^oil/(?P<pk>\d+)/update/', views.oilUpdate, 
        name="oil_update"),
    url(r'^oil/(?P<pk>\d+)/edit/', views.oilEdit, name="oil_edit"),
    url(r'^oil/(?P<pk>\d+)/', views.oilDetail, name="oil_detail"),
    url(r'^oil/create/', views.oilCreate, name="oil_create"),
    url(r'^oil/new/', views.oilNew, name="oil_new"),
    url(r'^oil/', views.oilIndex, name="oil_index"),
    
    url(r'^fuel/(?P<pk>\d+)/update/', views.fuelUpdate,
        name="fuel_update"),
    url(r'^fuel/(?P<pk>\d+)/edit/', views.fuelEdit, name="fuel_edit"),
    url(r'^fuel/(?P<pk>\d+)/', views.fuelDetail, name="fuel_detail"),
    url(r'^fuel/create/', views.fuelCreate, name="fuel_create"),
    url(r'^fuel/new/', views.fuelNew, name="fuel_new"),
    url(r'^fuel/', views.fuelIndex, name="fuel_index"),
    
    url(r'^', views.index, name="index"),
]
