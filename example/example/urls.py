from django.conf.urls import include, url
from django.http import HttpResponseNotFound

from django.contrib import admin
admin.autodiscover()


# A simple 404 renderer
def render404(request, exception):
    return HttpResponseNotFound('Not Found')
handler404 = 'example.urls.render404'


urlpatterns = [
    url(r'^inviter/', include('inviter2.urls')),
]
