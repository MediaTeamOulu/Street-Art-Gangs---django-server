from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from server import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^teams/$', views.TeamList.as_view()),
    url(r'^teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view()),
)


urlpatterns = format_suffix_patterns(urlpatterns)
