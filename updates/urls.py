from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^all/$', 'updates.views.all_updates'),
    url(r'^get/(?P<update_id>\d+)/$', 'updates.views.update'),
    
    url(r'^create/$', 'updates.views.create'),
    
    url(r'^json/$', 'updates.views.json_all'),
)