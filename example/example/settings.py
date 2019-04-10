"""
Example specific settings
"""
from example.default_settings import *

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'


INSTALLED_APPS = INSTALLED_APPS + [
    'inviter2',
    'example',
]

# Optional custom templates.  Default templates are used if these variables
# don't exist.
INVITER_FORM_TEMPLATE = 'custom_register.html'
INVITER_DONE_TEMPLATE = 'custom_done.html'
INVITER_OPTOUT_TEMPLATE = 'custom_optout.html'
INVITER_OPTOUT_DONE_TEMPLATE = 'custom_optout_done.html'
