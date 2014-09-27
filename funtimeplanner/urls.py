from django.conf.urls import patterns, url
from funtimeplanner import views
urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        #url(r'^interest/(?P<interest_name_url>\w+/$', views.interest, name='interest'),
        url(r'^event_matches/$', views.event_matches, name='event_matches'),
        url(r'^userlist/$', views.userlist_display, name='userlist'),
        )