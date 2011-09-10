import os, sys

#Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace) 

#Add the path to 3rd party django application and to django itself.
sys.path.append('/usr/local/lib/python2.7/dist-packages/django')
sys.path.append('/home/sean/MobileAC')

os.environ['DJANGO_SETTINGS_MODULE'] = 'MobileAC.settings_production'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
