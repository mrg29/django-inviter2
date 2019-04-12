from django.conf import settings, urls
from django.http import HttpResponseNotFound

from django.contrib import admin
admin.autodiscover()


# A simple 404 renderer
def render404(request, exception):
    return HttpResponseNotFound('Not Found')
handler404 = 'example.urls.render404'


urlpatterns = [
    urls.url(
        r'^inviter/',
        urls.include(('inviter2.urls', settings.INVITER_NAMESPACE))
    ),
]
