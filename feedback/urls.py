from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^all/$', 'feedback.views.all_feedback'),
    url(r'^get/(?P<fb_id>\d+)/$', 'feedback.views.feedback'),
    url(r'^parent_view/$', 'feedback.views.parent_view'),
    url(r'^parent_view_error/$', 'feedback.views.parent_view_error'),
    
    url(r'^create/$', 'feedback.views.create'),
    
    url(r'^json/$', 'feedback.views.json_all'),
)