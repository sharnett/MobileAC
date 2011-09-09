import os
import sys

path = '/home/sean/MobileAC/'
if path not in sys.path:
    sys.path.append(path)
sys.path.append('/usr/local/django')
sys.path.append('/usr/local/django/MobileAC')

os.environ['DJANGO_SETTINGS_MODULE'] = 'MobileAC.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
