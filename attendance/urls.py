from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^today/$',                  'attendance.views.attendance_today'),
    url(r'^get/(?P<att_id>\d+)/$',    'attendance.views.attendance_single'),
    
    url(r'^create/$',                 'attendance.views.create'),
    
    url(r'^json/$',                   'attendance.views.json_all'),
)