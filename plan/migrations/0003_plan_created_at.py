# Generated by Django 3.2.9 on 2021-12-01 22:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_alter_image_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
