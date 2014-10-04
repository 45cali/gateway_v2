# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='alert_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='jira_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='alerts',
            name='jira_time',
            field=models.TimeField(),
        ),
    ]
