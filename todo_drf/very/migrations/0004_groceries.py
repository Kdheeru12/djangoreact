# Generated by Django 3.1.5 on 2021-02-19 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('very', '0003_auto_20201218_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groceries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
            ],
        ),
    ]
