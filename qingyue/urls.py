from django.conf.urls import patterns, include, url
from django.contrib import admin
from demo1.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qingyue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', home),
)
