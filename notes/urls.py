from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^daily/(?P<pk>\d+)/edit/', views.daily_update, name="daily_edit"),
	url(r'^weekly/(?P<pk>\d+)/edit/', views.weekly_update, name="weekly_edit"),
]