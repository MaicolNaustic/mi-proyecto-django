import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'centro_fisioterapia.settings')

# Inicializa Django
django.setup()

# Ejecuta migraciones automáticamente al arrancar
from django.core.management import call_command
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Error ejecutando migraciones: {e}")

application = get_wsgi_application()
