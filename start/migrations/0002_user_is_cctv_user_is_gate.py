# Generated by Django 4.0.4 on 2022-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_cctv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_gate',
            field=models.BooleanField(default=False),
        ),
    ]