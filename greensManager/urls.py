"""greensManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

admin.site.site_header = 'GreensManager admin'
admin.site.site_title = 'GreensManager admin'

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^irrigation/', include('irrigation.urls', namespace="irr")),
    url(r'^shop/', include('machines.urls', namespace="shop")),
    url(r'^mow/', include('mowing.urls', namespace="mow")),
    url(r'^parts/', include('parts.urls', namespace="parts")),
    url(r'^turfs/', include('turfs.urls', namespace="turfs")),
    url(r'^fert/', include('fertilizing.urls', namespace="fert")),
    url(r'^notes/', include('notes.urls', namespace="notes")),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('welcome.urls', namespace="welcome"))
]
