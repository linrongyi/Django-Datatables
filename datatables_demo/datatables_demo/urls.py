from django.conf.urls import patterns, include, url
from django.conf import settings
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'^demo/load-once/$', 'demo.views.load_once_demo_view', name = 'load_once_demo'),
    url(r'^demo/server-side/$', 'demo.views.server_side_demo_view', name = 'server_side_demo'),
    url(r'^ajax/get-countries-list/$', 'demo.views.get_countries_list', name = 'get_countries_list'),
    url(r'^$', 'demo.views.index', name='index'),
    #url(r'^ajax/edit_cell', 'demo.views.edit_cell', name='edit_cell'),
    url(r'^ajax/edit_cell', 'demo.views.edit_cell', name='edit_cell'),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

