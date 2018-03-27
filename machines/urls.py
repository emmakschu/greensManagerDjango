from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^fairwaymow/(?P<pk>\d+)/update/', views.fairwaymowUpdate,
        name="fairwaymow_update"),
    url(r'^fairwaymow/(?P<pk>\d+)/edit/', views.fairwaymowEdit,
        name="fairwaymow_edit"),
    url(r'^fairwaymow/(?P<pk>\d+)/', views.fairwaymowDetail,
        name="fairwaymow_detail"),
    url(r'^fairwaymow/create/', views.fairwaymowCreate,
        name="fairwaymow_create"),
    url(r'^fairwaymow/new/', views.fairwaymowNew,
        name="fairwaymow_new"),
    url(r'^fairwaymow/', views.fairwaymowIndex,
        name="fairwaymow_index"),
    
    url(r'^teemow/(?P<pk>\d+)/update/', views.teemowUpdate,
        name="teemow_update"),
    url(r'^teemow/(?P<pk>\d+)/edit/', views.teemowEdit,
        name="teemow_edit"),
    url(r'^teemow/(?P<pk>\d+)/', views.teemowDetail,
        name="teemow_detail"),
    url(r'^teemow/create/', views.teemowCreate,
        name="teemow_create"),
    url(r'^teemow/new/', views.teemowNew, name="teemow_new"),
    url(r'^teemow/', views.teemowIndex, name="teemow_index"),
    
    url(r'^greensmow/(?P<pk>\d+)/update/', views.greensmowUpdate,
        name="greensmow_update"),
    url(r'^greensmow/(?P<pk>\d+)/edit/', views.greensmowEdit,
        name="greensmow_edit"),
    url(r'^greensmow/(?P<pk>\d+)/', views.greensmowDetail,
        name="greensmow_detail"),
    url(r'^greensmow/create/', views.greensmowCreate,
        name="greensmow_create"),
    url(r'^greensmow/new/', views.greensmowNew,
        name="greensmow_new"),
    url(r'^greensmow/', views.greensmowIndex, name="greensmow_index"),
    
    url(r'^', views.index, name="index"),
]
