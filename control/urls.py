from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('control.views',
   url(r'', 'index'),
)
