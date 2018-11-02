from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'mow', views.mowTaskIndex, name="mowIndex"),
    url(r'^', views.index, name="index"),
]
