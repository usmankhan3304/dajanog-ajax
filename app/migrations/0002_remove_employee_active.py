# Generated by Django 5.0.1 on 2024-04-04 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='active',
        ),
    ]