"""
WSGI config for websiteDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from webvars import git

import threading

def update():
    threading.Timer(60, update).start
    git.updateAll()

update()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websiteDjango.settings')

application = get_wsgi_application()
