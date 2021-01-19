# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/kdogk9/Django-E-Commerce/perfectcushion/settings.py'
path = '/home/kdogk9/projects/Django-E-Commerce'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'perfectcushion.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "perfectcushion.settings")

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

