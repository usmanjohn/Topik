# Generated by Django 5.0.6 on 2024-06-28 15:23

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("topics", "0010_alter_topic_topic_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="additional_text",
            field=django_ckeditor_5.fields.CKEditor5Field(
                blank=True, default="none", null=True, verbose_name="Additional"
            ),
        ),
    ]
