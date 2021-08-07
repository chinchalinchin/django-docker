from django.contrib.auth.models import User, Group

from core import settings

def create_superuser(apps, schema_editor):
    admin_group = Group.objects.get(name='administrator')
    superuser = User.objects.create_superuser(username=settings.SUPERUSER_USERNAME,
                                    password=settings.SUPERUSER_PASSWORD,
                                    email=settings.SUPERUSER_EMAIL)
    admin_group.user_set.add(superuser)