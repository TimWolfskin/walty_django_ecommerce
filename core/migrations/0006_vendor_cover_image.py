# Generated by Django 5.0.1 on 2024-02-03 12:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_vendor_date_alter_product_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(default='vendor.jpg', upload_to=core.models.user_directory_path),
        ),
    ]
