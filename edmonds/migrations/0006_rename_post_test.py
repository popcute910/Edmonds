# Generated by Django 3.2.16 on 2022-11-26 08:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edmonds', '0005_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='TEST',
        ),
    ]
