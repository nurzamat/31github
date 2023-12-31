# Generated by Django 4.2.7 on 2023-12-12 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='comments', to='api.post')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
