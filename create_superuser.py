import os
import sys
import django
from django.core.management import call_command
from django.contrib.auth import get_user_model


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'terraflora')))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terraflora.settings')


django.setup()

def create_superuser():
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        print('Superusuário criado com sucesso.')
    else:
        print('Superusuário já existe.')

def setup_database():

    call_command('migrate')
    create_superuser()

if __name__ == '__main__':
    setup_database()
