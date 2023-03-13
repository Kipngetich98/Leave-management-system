# Generated by Django 2.2.5 on 2021-05-24 06:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyleave', '0046_auto_20190119_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapplication',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 14, 53, 39, 281400), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplication',
            name='status',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('APPROVED', 'APPROVED'), ('DECLINED', 'DECLINED')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='applied_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 24, 14, 53, 39, 284397), null=True),
        ),
        migrations.AlterField(
            model_name='leaveapplicationdetails',
            name='status',
            field=models.CharField(choices=[('Choose...', 'Choose...'), ('APPROVED', 'APPROVED'), ('DECLINED', 'DECLINED')], max_length=50, null=True),
        ),
    ]