# Generated by Django 3.1.5 on 2021-01-10 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('ticketopen', models.DateTimeField(default=datetime.datetime.now)),
                ('ticketend', models.DateTimeField()),
            ],
        ),
    ]
