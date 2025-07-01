import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centro_fisioterapia.settings')

# Ejecutar migraciones automáticamente
django.setup()
from django.core.management import call_command
call_command('migrate')

application = get_wsgi_application()
