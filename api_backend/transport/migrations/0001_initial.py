# Generated by Django 2.2.2 on 2020-09-16 18:58

from django.db import migrations, models
import django.db.models.deletion
import transport.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.CharField(default=transport.models.uuid_str, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('country', models.IntegerField(choices=[(1, 'United States'), (2, 'Russia'), (3, 'China'), (4, 'Germany'), (5, 'United Kingdom'), (6, 'France'), (7, 'Japan'), (8, 'Israel'), (9, 'India'), (10, 'Canada')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'manufacturers',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.CharField(default=transport.models.uuid_str, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('number_of_doors', models.IntegerField()),
                ('price', models.FloatField()),
                ('model_name', models.CharField(max_length=100)),
                ('owner', models.CharField(blank=True, max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transport.Manufacturer')),
            ],
            options={
                'db_table': 'cars',
            },
        ),
    ]