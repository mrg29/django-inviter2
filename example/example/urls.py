from django.conf.urls import patterns, include, url
from django.http import HttpResponseNotFound

from django.contrib import admin
admin.autodiscover()


# A simple 404 renderer for Django 1.4
def render404(request):
    return HttpResponseNotFound('Not Found')
handler404 = 'example.urls.render404'


urlpatterns = patterns(
    '',
    url(r'^inviter/', include('inviter2.urls', namespace='inviter2')),
)
