from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^greensmower/(?P<mower_id>[0-9]+)', views.mower, name="mowerDetail"),
    url(r'^', views.index, name="index"),
]
