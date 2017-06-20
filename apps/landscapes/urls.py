from django.conf.urls import url
from . import views
app_name = 'landscapes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<num>.+)$', views.image, name='image')
]
