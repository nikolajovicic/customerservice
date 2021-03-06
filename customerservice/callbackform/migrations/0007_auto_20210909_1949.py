# Generated by Django 3.2.7 on 2021-09-09 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callbackform', '0006_alter_supportrequest_callback_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportrequest',
            name='callback_date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supportrequest',
            name='callback_time',
            field=models.TimeField(blank=True, choices=[('09:00', datetime.time(9, 0)), ('09:30', datetime.time(9, 30)), ('10:00', datetime.time(10, 0))], null=True),
        ),
    ]
