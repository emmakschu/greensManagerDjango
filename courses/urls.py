from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^bunker/(?P<pk>\d+)/edit/', 
		views.bunker_update, 
		name="bunker_update"),
	url(r'^bunker/(?P<pk>\d+)/', 
		views.bunker_detail, 
		name="bunker_detail"),
	url(r'^bunker/', views.bunker_index, name="bunker_index"),

	url(r'^rough/(?P<pk>\d+)/edit/', 
		views.rough_update, 
		name="rough_update"),
	url(r'^rough/(?P<pk>\d+)/', 
		views.rough_detail, 
		name="rough_detail"),
	url(r'^rough/', views.rough_index, name="rough_index"),

	url(r'^green/(?P<pk>\d+)/edit/', 
		views.green_update, 
		name="green_update"),
	url(r'^green/(?P<pk>\d+)/', 
		views.green_detail, 
		name="green_detail"),
	url(r'^green/', views.green_index, name="green_index"),

	url(r'^fairway/(?P<pk>\d+)/edit/', 
		views.fairway_update, 
		name="fairway_update"),
	url(r'^fairway/(?P<pk>\d+)/', 
		views.fairway_detail, 
		name="fairway_detail"),
	url(r'^fairway/', views.fairway_index, name="fairway_index"),

	url(r'^tee/(?P<pk>\d+)/edit/', 
		views.tee_update, 
		name="tee_update"),
	url(r'^tee/(?P<pk>\d+)/', 
		views.tee_detail, 
		name="tee_detail"),
	url(r'^tee/', views.tee_index, name="tee_index"),

	url(r'^hole/(?P<pk>\d+)/', 
		views.hole_detail, 
		name="hole_detail"),
	url(r'^hole/', views.hole_index, name="hole_index"),

	url(r'^(?P<pk>\d+)/', 
		views.course_detail, 
		name="course_detail"),

    url(r'^', views.index, name="index"),
]
