from django.conf.urls import url

from . import views

app_name = 'stimp'
urlpatterns = [
    
    url(r'^(?P<pk>\d+)/', views.detail, name="detail"),
    url(r'^create/', views.create, name="create"),
    url(r'^new/', views.new, name="new"),
    url(r'^', views.index, name="index"),
]
