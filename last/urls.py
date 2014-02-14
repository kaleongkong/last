from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'last.views.home', name='home'),
    url(r'^', include('login.urls', namespace="login")),

    url(r'^admin/', include(admin.site.urls)),
)
