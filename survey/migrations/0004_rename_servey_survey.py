# Generated by Django 3.2.9 on 2021-12-02 01:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_plan_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('survey', '0003_alter_servey_patricipants'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Servey',
            new_name='Survey',
        ),
    ]
