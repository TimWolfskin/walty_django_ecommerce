# Generated by Django 5.0.1 on 2024-02-11 07:35

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_address_mobile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WishList',
            new_name='WishList_model',
        ),
    ]
