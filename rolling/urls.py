from django.conf.urls import url 

from . import views

app_name = 'roll'
urlpatterns = [
    
    url(r'^tees/(?P<pk>\d+)/update/', views.teesUpdate,
        name="tees_update"),
    url(r'^tees/(?P<pk>\d+)/edit/', views.teesEdit, name="tees_edit"),
    url(r'^tees/(?P<pk>\d+)/', views.teesDetail, name="tees_detail"),
    url(r'^tees/create/', views.teesCreate, name="tees_create"),
    url(r'^tees/new/', views.teesNew, name="tees_new"),
    url(r'^tees/', views.teesIndex, name="tees_index"),
    
    url(r'^greens/(?P<pk>\d+)/update/', views.greensUpdate,
        name="greens_update"),
    url(r'^greens/(?P<pk>\d+)/edit/', views.greensEdit,
        name="greens_edit"),
    url(r'^greens/(?P<pk>\d+)/', views.greensDetail, 
        name="greens_detail"),
    url(r'^greens/create/', views.greensCreate, name="greens_create"),
    url(r'^greens/new/', views.greensNew, name="greens_new"),
    url(r'^greens/', views.greensIndex, name="greens_index"),
    
]
