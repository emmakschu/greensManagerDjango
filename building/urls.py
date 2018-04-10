from django.conf.urls import url 

from . import views

urlpatterns = [
    
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
