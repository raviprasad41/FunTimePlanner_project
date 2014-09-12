from django.conf.urls import patterns, url
from funtimeplanner import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),

        )