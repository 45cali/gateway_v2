# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_status', models.IntegerField(max_length=1, choices=[(0, b'new'), (1, b'created'), (2, b'updated')])),
                ('monitoring_server_name', models.CharField(max_length=255)),
                ('alert_hostname', models.CharField(max_length=255)),
                ('alert_name', models.CharField(max_length=255)),
                ('alert_status', models.IntegerField(max_length=1, choices=[(0, b'clear'), (1, b'info'), (2, b'warning'), (3, b'critical'), (4, b'major')])),
                ('alert_detail', models.CharField(max_length=255)),
                ('time', models.TimeField(auto_now=True, auto_now_add=True)),
                ('date', models.DateField(auto_now=True, auto_now_add=True)),
                ('jira_ticket', models.CharField(max_length=255)),
                ('jira_time', models.TimeField(auto_now=True, auto_now_add=True)),
                ('jira_date', models.DateField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'id',
            },
            bases=(models.Model,),
        ),
    ]
