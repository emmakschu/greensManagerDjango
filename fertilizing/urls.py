from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^fertilizers/(?P<pk>\d+)/update/',
        views.fertUpdate, name="fert_update"),
    url(r'^fertilizers/(?P<pk>\d+)/edit/',
        views.fertEdit, name="fert_edit"),
    url(r'^fertilizers/(?P<pk>\d+)/', 
        views.fertDetail, name="fert_detail"),
    url(r'^fertilizers/create/', views.createFert, name="create_fert"),
    url(r'^fertilizers/new/', views.newFert, name="new_fert"),
    url(r'^fertilizers/', views.fert_index, name="fert_index"),
    
    url(r'^', views.index, name="index"),
]
