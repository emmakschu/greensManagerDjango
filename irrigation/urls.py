from django.conf.urls import url

from . import views

urlpatterns = [
    
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
