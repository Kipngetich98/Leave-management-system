# Generated by Django 2.1 on 2018-11-23 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0010_auto_20181123_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 23, 13, 46, 29, 315459), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
