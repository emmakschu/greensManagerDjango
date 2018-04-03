from djagno.utils import url

from . import views

urlpatterns = [
    
    url(r'^', views.index, name="index"),
]
