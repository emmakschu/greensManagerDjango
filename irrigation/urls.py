from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^sprinkler/(?P<pk>\d+)/update/', views.sprinklerUpdate,
        name="sprinkler_update"),
    url(r'^sprinkler/(?P<pk>\d+)/edit/', views.sprinklerEdit,
        name="sprinkler_edit"),
    url(r'^sprinkler/(?P<pk>\d+)/', views.sprinklerDetail,
        name="sprinkler_detail"),
    url(r'^sprinkler/create/', views.sprinklerCreate,
        name="sprinkler_create"),
    url(r'^sprinkler/new/', views.sprinklerNew,
        name="sprinkler_new"),
    url(r'^sprinkler/', views.sprinklerIndex,
        name="sprinkler_index"),
    
    url(r'^satbox/(?P<pk>\d+)/update/',
        views.satboxUpdate, name="satbox_update"),
    url(r'^satbox/(?P<pk>\d+)/edit/',
        views.satboxEdit, name="satbox_edit"),
    url(r'^satbox/(?P<pk>\d+)/',
        views.satboxDetail, name="satbox_detail"),
    url(r'^satbox/create/', views.satboxCreate, name="satbox_create"),
    url(r'^satbox/new/', views.satboxNew, name="satbox_new"),
    url(r'^satbox/', views.satboxIndex, name="satbox_index"),
    
    url(r'^$', views.index, name="index"),
]
