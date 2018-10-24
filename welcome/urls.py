from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^daily/', views.daily, name="daily"),
    url(r'^login/', views.login_page, name="login"),
    url(r'^', views.index, name="index"),
]
