# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2198846/data/www/admiral.kg/Admiral')
sys.path.insert(1, '/var/www/u2198846/data/admiral-venv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Admiral.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()