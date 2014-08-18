from django.conf.urls.defaults import patterns, include, url
from yousharizvi.yousha.views import *


urlpatterns = patterns('',
    # Examples:
    url(r'^$', home.as_view()),
)
