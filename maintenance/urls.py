from django.conf.urls import url

from . import views

urlpatterns = [
    
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
