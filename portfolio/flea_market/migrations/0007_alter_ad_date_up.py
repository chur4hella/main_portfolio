# Generated by Django 3.2.6 on 2021-10-11 21:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0006_alter_ad_date_up'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 21, 44, 45, 672450, tzinfo=utc)),
        ),
    ]
