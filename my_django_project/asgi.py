"""
ASGI config for my_django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

<<<<<<< HEAD

import os, sys
import os, copy
=======
import os, sys

import json

>>>>>>> 678af1f4e0fb1590bb857259505b5014789bb641

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

application = get_asgi_application()
