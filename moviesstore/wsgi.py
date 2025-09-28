"""
WSGI config for movesstore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

path = '/home/g2017010469/moviestore'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'moviesstore.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesstore.settings')

application = get_wsgi_application()
