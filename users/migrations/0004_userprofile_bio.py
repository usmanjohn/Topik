# Generated by Django 5.0.6 on 2024-05-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(default='I did not write a bio yet', max_length=150),
            preserve_default=False,
        ),
    ]
