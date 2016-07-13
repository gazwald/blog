from django.conf.urls import url

from . import views

app_name = 'media'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.file_add, name='file_add'),
]
