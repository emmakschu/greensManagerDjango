from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new', views.newFert),
    url(r'^', views.index),
]