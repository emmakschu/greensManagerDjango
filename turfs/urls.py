from django.conf.urls import url

from . import views

app_name = 'turfs'
urlpatterns = [
    url(r'^$', views.index),
]
