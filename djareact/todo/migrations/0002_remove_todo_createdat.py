# Generated by Django 3.0.7 on 2020-12-07 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='createdAt',
        ),
    ]
