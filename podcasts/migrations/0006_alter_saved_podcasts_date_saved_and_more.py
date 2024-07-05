# Generated by Django 5.0.6 on 2024-07-05 04:15

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0005_alter_saved_podcasts_date_saved'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved_podcasts',
            name='date_saved',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 5, 4, 14, 37, 567613, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='saved_podcasts',
            unique_together={('user', 'podcast')},
        ),
        migrations.AlterField(
            model_name='saved_podcasts',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_podcasts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='saved_podcasts',
            name='podcast',
        ),
        migrations.AddField(
            model_name='saved_podcasts',
            name='podcast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='saved_by', to='podcasts.podcast'),
            preserve_default=False,
        ),
    ]