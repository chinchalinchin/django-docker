from django.contrib.auth.models import Group
from core import settings

def create_groups(apps, schema_editor):
    for group in settings.GROUPS:
        Group.objects.create(name=group)