from django.conf.urls import url

from . import views

# TODO: Adjust URLs to handle potential redirects to calling page after logging in
app_name = 'welcome'
urlpatterns = [
    url(r'^daily/', views.daily, name="daily"),
    url(r'^login/', views.login_page, name="login"),
    url(r'^', views.index, name="index"),
]
