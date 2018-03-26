from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^dig/(?P<pk>\d+)/update/', views.digUpdate, 
        name="dig_update"),
    url(r'^dig/(?P<pk>\d+)/edit/', views.digEdit, name="dig_edit"),
    url(r'^dig/(?P<pk>\d+)/', views.digDetail, name="dig_detail"),
    url(r'^dig/create/', views.digCreate, name="dig_create"),
    url(r'^dig/new/', views.digNew, name="dig_new"),
    url(r'^dig/', views.digIndex, name="dig_index"),
    
    url(r'^iso/(?P<pk>\d+)/update/', views.isoUpdate,
        name="iso_update"),
    url(r'^iso/(?P<pk>\d+)/edit/', views.isoEdit, name="iso_edit"),
    url(r'^iso/(?P<pk>\d+)/', views.isoDetail, name="iso_detail"),
    url(r'^iso/create/', views.isoCreate, name="iso_create"),
    url(r'^iso/new/', views.isoNew, name="iso_new"),
    url(r'^iso/', views.isoIndex, name="iso_index"),
    
    url(r'^drain/(?P<pk>\d+)/update/', views.drainUpdate,
        name="drain_update"),
    url(r'^drain/(?P<pk>\d+)/edit/', views.drainEdit,
        name="drain_edit"),
    url(r'^drain/(?P<pk>\d+)/', views.drainDetail,
        name="drain_detail"),
    url(r'^drain/create/', views.drainCreate, name="drain_create"),
    url(r'^drain/new/', views.drainNew, name="drain_new"),
    url(r'^drain/', views.drainIndex, name="drain_index"),
    
    url(r'^qc/(?P<pk>\d+)/update/', views.qcUpdate, name="qc_update"),
    url(r'^qc/(?P<pk>\d+)/edit/', views.qcEdit, name="qc_edit"),
    url(r'^qc/(?P<pk>\d+)/', views.qcDetail, name="qc_detail"),
    url(r'^qc/create/', views.qcCreate, name="qc_create"),
    url(r'^qc/new/', views.qcNew, name="qc_new"),
    url(r'^qc/', views.qcIndex, name="qc_index"),
        
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
