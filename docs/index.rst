Welcome to django-inviter2's documentation!
===========================================

django-inviter2 allows you to invite users to your Django application. Invited
users are saved as inactive users in your database and activated upon
registration.

Installation
------------

::

    pip install django-inviter2


Configuration
-------------

Add ``inviter2`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        'inviter2'
    )

Include :attr:`inviter2.urls` into your root ``urls.py`` file under the ``inviter2`` namespace

::

    urlpatterns = patterns(
        # [...]
        url('^invites/', include('inviter2.urls', namespace='inviter2'),
    )



Usage
-----

To invite people make use of :attr:`inviter2.utils.invite`

::

    from inviter2.utils import invite

    invite("foo@example.com", request.user, current_time=datetime.now())

:attr:`inviter2.utils.invite` also allows you to make use of a custom email
sending function, say to send HTML emails

::

    from inviter2.utils import invite

    def sendhtml(invitee, inviter, **kwargs):
        # Load templates, send the email here
        pass

    invite("foo@example.com", request.user, sendfn=sendhtml)

A useful application of this is keeping track of who invites whom:

::

    from inviter2 import utils
    from app.models import Invites

    def send(invitee, inviter, **kwargs):
        Invites.objects.get_or_create(invitee=invitee, inviter=inviter)
        utils.send_invite(invitee, inviter, **kwargs)

    utils.invite("foo@example.com", request.user, sendfn=send)

Consult :attr:`inviter2.utils.invite` and
:attr:`inviter2.utils.send_invite` for more
information.

By default :attr:`inviter2.utils.send_invite` will render
``inviter2/email/subject.txt``
and ``inviter2/email/body.txt`` for the email.

``templates/inviter2/register.html`` and ``templates/inviter2/done.html``
are rendered when registering respectively when done.

If you need a post registration hook, override the registration form with the
settings below.


Settings
--------

There are a couple of editable settings

.. attribute:: INVITER_FORM

    :Default: :class:`inviter2.forms.RegistrationForm`
    :type: str

    The form to be used when an invited user signs up.

.. attribute:: INVITER_REDIRECT

    :Default: ``'inviter2:done'``
    :type: str

    The URL to redirect the user to when the signup completes. This is either a
    URL to reverse via ``reverse(INVITER_REDIRECT)`` or a simple string.
    Reversing the URL is tried before using the string.

.. attribute:: INVITER_TOKEN_GENERATOR

    :Default: ``'inviter2.tokens.generator'``
    :type: str

    The generator used to create a token which is used to assemble an invite
    URL

.. attribute:: INVITER_FROM_EMAIL

    :Default: ``settings.DEFAULT_FROM_EMAIL``

    The email address used to send invites from

.. attribute:: INVITER_FORM_TEMPLATE

    :Default: ``None``

    Allows the user to specify a custom template for the inviter form.

.. attribute:: INVITER_DONE_TEMPLATE

    :Default: ``None``

    Allows the user to specify a custom template for the done view.

.. attribute:: INVITER_OPTOUT_TEMPLATE

    :Default: ``None``

    Allows the user to specify a custom template for the opt-out view.

.. attribute:: INVITER_OPTOUT_DONE_TEMPLATE

    :Default: ``None``

    Allows the user to specify a custom template for the opt-out done view.

API
---

.. toctree::
    :maxdepth: 3

    inviter2
