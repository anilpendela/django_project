"""
ASGI config for my_django_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

<<<<<<< HEAD
import os, sys
=======
import os, copy
>>>>>>> 3e83ea5c3e6fa64eaeb0835d66618cab06965291

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_django_project.settings')

application = get_asgi_application()
