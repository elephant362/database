# Generated by Django 5.1.6 on 2025-03-28 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mi_app', '0002_delete_sensordata'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.FloatField()),
                ('humedad', models.FloatField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
