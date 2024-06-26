# Generated by Django 5.0.6 on 2024-05-22 13:24

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
            name='TopicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_title', models.CharField(max_length=150)),
                ('topic_body', models.TextField()),
                ('topic_hashtag', models.CharField(max_length=50)),
                ('topic_pub_date', models.DateField(auto_now_add=True)),
                ('topic_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_auth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TopicAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_body', models.TextField()),
                ('answer_pub_date', models.DateField(auto_now_add=True)),
                ('answer_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_auth', to=settings.AUTH_USER_MODEL)),
                ('topic_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='topics.topiccontent')),
            ],
        ),
        migrations.CreateModel(
            name='Upvoter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.SmallIntegerField(choices=[(1, 'upvote'), (-1, 'downvote')])),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='topics.topiccontent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
