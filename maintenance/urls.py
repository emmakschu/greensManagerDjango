from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^request/submit', views.repairRequest,
        name="repair_request"),
    url(r'^request/', views.repairNeeded, name="repair_needed"),
    
    url(r'^repair/(?P<pk>\d+)/update/', views.repairUpdate,
        name="repair_update"),
    url(r'^repair/(?P<pk>\d+)/edit/', views.repairEdit,
        name="repair_edit"),
    url(r'^repair/(?P<pk>\d+)/', views.repairDetail,
        name="repair_detail"),
    url(r'^repair/create/', views.repairCreate,
        name="repair_create"),
    url(r'^repair/new/', views.repairNew, name="repair_new"),
    url(r'^repair/', views.repairIndex, name="repair_index"),
    
    url(r'^oil/(?P<pk>\d+)/update/', views.oilchangeUpdate,
        name="oilchange_update"),
    url(r'^oil/(?P<pk>\d+)/edit/', views.oilchangeEdit,
        name="oilchange_edit"),
    url(r'^oil/(?P<pk>\d+)/', views.oilchangeDetail,
        name="oilchange_detail"),
    url(r'^oil/create/', views.oilchangeCreate,
        name="oilchange_create"),
    url(r'^oil/new/', views.oilchangeNew, name="oilchange_new"),
    url(r'^oil/', views.oilchangeIndex, name="oilchange_index"),
    
]
