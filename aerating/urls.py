from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^greens/(?P<pk>\d+)/update/', views.greensUpdate,
        name="greens_update"),
    url(r'^greens/(?P<pk>\d+)/edit/', views.greensEdit,
        name="greens_edit"),
    url(r'^greens/(?P<pk>\d+)/', views.greensDetail,
        name="greens_detail"),
    url(r'^greens/create/', views.greensCreate, name="greens_create"),
    url(r'^greens/new/', views.greensNew, name="greens_new"),
    url(r'^greens/', views.greensIndex, name="greens_index"),
    
    url(r'^', views.index, name="index"),
]
