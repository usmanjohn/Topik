# Generated by Django 5.0.6 on 2024-07-02 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('hiring_company', models.CharField(max_length=70)),
                ('position', models.CharField(max_length=50)),
                ('required_skills', models.TextField(blank=True, null=True)),
                ('required_tools', models.TextField(blank=True, null=True)),
                ('images', models.ImageField(default='jobs/default.png', upload_to='jobs')),
                ('role', models.TextField(blank=True, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('company_links', models.URLField(blank=True, null=True)),
                ('uploader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
