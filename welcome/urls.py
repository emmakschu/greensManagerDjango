from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^daily/', views.daily, name="daily"),
    url(r'^', views.index, name="index"),
]
