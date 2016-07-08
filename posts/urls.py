from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.post_add, name='post_add'),
    url(r'^(?P<post_id>[0-9]+)$', views.post_view, name='post_view'),
]
