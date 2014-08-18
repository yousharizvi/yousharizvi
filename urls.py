from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from yousha.views import contact

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('yousharizvi.yousha.urls')),
    url(r'^home/', include('yousharizvi.yousha.urls')),
	url(r'^contact/$', contact),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)