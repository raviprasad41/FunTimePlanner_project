from django.conf.urls import patterns, url
from funtimeplanner import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^interest/(?P<interest_name_url>\w+/$', views.interest, name='interest'),

        )