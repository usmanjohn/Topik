# Generated by Django 5.0.6 on 2024-07-08 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='role',
            new_name='qualifications',
        ),
    ]
