# Generated by Django 4.2.7 on 2023-12-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_postcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='middle_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
