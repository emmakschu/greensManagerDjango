from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^search/', views.partsSearch, name="parts_search"),
    
    url(r'^filter/(?P<pk>\d+)/update/', views.filterUpdate,
        name="filter_update"),
    url(r'^filter/(?P<pk>\d+)/edit/', views.filterEdit,
        name="filter_edit"),
    url(r'^filter/(?P<pk>\d+)/', views.filterDetail, 
        name="filter_detail"),
    url(r'^filter/create/', views.filterCreate, name="filter_create"),
    url(r'^filter/new/', views.filterNew, name="filter_new"),
    url(r'^filter/', views.filterIndex, name="filter_index"),
    
    url(r'^part/(?P<pk>\d+)/update/', views.partUpdate,
        name="part_update"),
    url(r'^part/(?P<pk>\d+)/edit/', views.partEdit,
        name="part_edit"),
    url(r'^part/(?P<pk>\d+)/', views.partDetail, name="part_detail"),
    url(r'^part/create/', views.partCreate, name="part_create"),
    url(r'^part/new/', views.partNew, name="part_new"),
    url(r'^part/', views.partIndex, name="part_index"),
    
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
