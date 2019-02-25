from django.conf.urls import url

from . import views

app_name = 'courses'
urlpatterns = [

	url(r'^bunkers/(?P<pk>\d+)/edit/', 
		views.bunker_update, 
		name="bunker_update"),
	url(r'^bunkers/(?P<pk>\d+)/', 
		views.bunker_detail, 
		name="bunker_detail"),
	url(r'^bunkers/', views.bunker_index, name="bunker_index"),

	url(r'^roughs/(?P<pk>\d+)/edit/', 
		views.rough_update, 
		name="rough_update"),
	url(r'^roughs/(?P<pk>\d+)/', 
		views.rough_detail, 
		name="rough_detail"),
	url(r'^roughs/', views.rough_index, name="rough_index"),

	url(r'^greens/(?P<pk>\d+)/edit/', 
		views.green_update, 
		name="green_update"),
	url(r'^greens/(?P<pk>\d+)/', 
		views.green_detail, 
		name="green_detail"),
	url(r'^greens/', views.green_index, name="green_index"),

	url(r'^fairways/(?P<pk>\d+)/edit/', 
		views.fairway_update, 
		name="fairway_update"),
	url(r'^fairways/(?P<pk>\d+)/', 
		views.fairway_detail, 
		name="fairway_detail"),
	url(r'^fairways/', views.fairway_index, name="fairway_index"),

	url(r'^tees/(?P<pk>\d+)/edit/', 
		views.tee_update, 
		name="tee_update"),
	url(r'^tees/(?P<pk>\d+)/', 
		views.tee_detail, 
		name="tee_detail"),
	url(r'^tees/', views.tee_index, name="tee_index"),

	url(r'^holes/(?P<pk>\d+)/', 
		views.hole_detail, 
		name="hole_detail"),
	url(r'^holes/', views.hole_index, name="hole_index"),

	url(r'^(?P<pk>\d+)/', 
		views.course_detail, 
		name="course_detail"),

    url(r'^', views.index, name="index"),
]
