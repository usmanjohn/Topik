# Generated by Django 5.0.6 on 2024-06-25 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_facebook_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='link_image',
            field=models.ImageField(default='links/personal_profile.png', upload_to='links'),
        ),
    ]