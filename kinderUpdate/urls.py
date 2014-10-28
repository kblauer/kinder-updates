from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kinderUpdate.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Site wide urls
    url(r'^$', 'kinderUpdate.views.home', name='home'),

    # Django admin url
    url(r'^admin/', include(admin.site.urls)),

    # User authentication urls
    url(r'^user/auth/$',      'kinderUpdate.views.auth_view'),
    url(r'^user/logout/$',    'kinderUpdate.views.logout'),
    # url(r'^user/loggedin/$',  'kinderUpdate.views.loggedin'),
    url(r'^user/invalid/$',   'kinderUpdate.views.invalid_login'),
    
    
    # App-related urls
    url(r'^updates/', include('updates.urls')),
    
)
