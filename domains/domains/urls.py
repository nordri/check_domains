from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # View -> Domains
    url(r'^$', 'check_domains.views.view_domain', name='view_domain'),
    # ability to filter
    url(r'^filter/(?P<days_left>\d+)/$', 'check_domains.views.view_domain'),
    url(r'^filter/$', 'check_domains.views.filterByDays'),
    # admin interface
    url(r'^admin/', include(admin.site.urls)),
)
