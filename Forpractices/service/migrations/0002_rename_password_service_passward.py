# Generated by Django 4.1.3 on 2022-11-17 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='password',
            new_name='passward',
        ),
    ]