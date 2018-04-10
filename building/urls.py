from django.conf.urls import url 

from . import views

urlpatterns = [
    
    url(r'^bunker/(?P<pk>\d+)/update/', views.bunkerUpdate,
        name="bunker_update"),
    url(r'^bunker/(?P<pk>\d+)/edit/', views.bunkerEdit,
        name="bunker_edit"),
    url(r'^bunker/(?P<pk>\d+)/', views.bunkerDetail,
        name="bunker_detail"),
    url(r'^bunker/create/', views.bunkerCreate, name="bunker_create"),
    url(r'^bunker/new/', views.bunkerNew, name="bunker_new"),
    url(r'^bunker/', views.bunkerIndex, name="bunker_index"),
    
    url(r'^fairway/(?P<pk>\d+)/update/', views.fairwayUpdate,
        name="fairway_update"),
    url(r'^fairway/(?P<pk>\d+)/edit/', views.fairwayEdit,
        name="fairway_edit"),
    url(r'^fairway/(?P<pk>\d+)/', views.fairwayDetail,
        name="fairway_detail"),
    url(r'^fairway/create/', views.fairwayCreate, 
        name="fairway_create"),
    url(r'^fairway/new/', views.fairwayNew, name="fairway_new"),
    url(r'^fairway/', views.fairwayIndex, name="fairway_index"),
    
    url(r'^tee/(?P<pk>\d+)/update', views.teeUpdate, 
        name="tee_update"),
    url(r'^tee/(?P<pk>\d+)/edit/', views.teeEdit, name="tee_edit"),
    url(r'^tee/(?P<pk>\d+)/', views.teeDetail, name="tee_detail"),
    url(r'^tee/create', views.teeCreate, name="tee_create"),
    url(r'^tee/new/', views.teeNew, name="tee_new"),
    url(r'^tee/', views.teeIndex, name="tee_index"),
    
    url(r'^green/(?P<pk>\d+)/update/', views.greenUpdate,
        name="green_update"),
    url(r'^green/(?P<pk>\d+)/edit/', views.greenEdit,
        name="green_edit"),
    url(r'^green/(?P<pk>\d+)/', views.greenDetail, 
        name="green_detail"),
    url(r'^green/create/', views.greenCreate, name="green_create"),
    url(r'^green/new/', views.greenNew, name="green_new"),
    url(r'^green/', views.greenIndex, name="green_index"),
]
