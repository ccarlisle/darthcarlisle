from django.conf.urls import patterns, include, url
from darthcarlisle.views import HomeView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^home/',HomeView.as_view())
    # Examples:
    # url(r'^$', 'darthcarlisle.views.home', name='home'),
    # url(r'^darthcarlisle/', include('darthcarlisle.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
