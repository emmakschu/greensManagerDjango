from django.conf.urls import url 

from . import views

app_name = 'topdress'
urlpatterns = [
    
    url(r'^fairways/(?P<pk>\d+)/update/', views.fairwaysUpdate,
        name="fairways_update"),
    url(r'^fairways/(?P<pk>\d+)/edit/', views.fairwaysEdit,
        name="fairways_edit"),
    url(r'^fairways/(?P<pk>\d+)/', views.fairwaysDetail,
        name="fairways_detail"),
    url(r'^fairways/create/', views.fairwaysCreate,
        name="fairways_create"),
    url(r'^fairways/new/', views.fairwaysNew, name="fairways_new"),
    url(r'^fairways/', views.fairwaysIndex, name="fairways_index"),
    
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
    
    url(r'^sand/(?P<pk>\d+)/update', views.sandUpdate, 
        name="sand_update"),
    url(r'^sand/(?P<pk>\d+)/edit', views.sandEdit, name="sand_edit"),
    url(r'^sand/(?P<pk>\d+)/', views.sandDetail, name="sand_detail"),
    url(r'^sand/create/', views.sandCreate, name="sand_create"),
    url(r'^sand/new/', views.sandNew, name="sand_new"),
    url(r'^sand/', views.sandIndex, name="sand_index"),
    
    url(r'^', views.index, name="index"),
]
