from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # View -> Domains
    url(r'^$', 'check_domains.views.view_domain', name='view_domain'),

    url(r'^admin/', include(admin.site.urls)),
)
