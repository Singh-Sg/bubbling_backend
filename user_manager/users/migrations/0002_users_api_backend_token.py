# Generated by Django 2.2.2 on 2020-09-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='api_backend_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
