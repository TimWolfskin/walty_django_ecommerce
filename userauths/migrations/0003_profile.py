# Generated by Django 5.0.1 on 2024-02-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
                ('full_name', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
    ]
