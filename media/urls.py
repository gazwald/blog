from django.conf.urls import url

from . import views

app_name = 'media'
urlpatterns = [
    url(r'^$', views.media_list, name='media_list'),
    url(r'^add/$', views.media_add, name='media_add'),
    url(r'^del/$', views.media_del, name='media_del'),
]
