# Generated by Django 2.2 on 2019-05-05 19:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20190430_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
