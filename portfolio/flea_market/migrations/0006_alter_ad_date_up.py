# Generated by Django 3.2.6 on 2021-10-11 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0005_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_up',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 11, 21, 41, 32, 597366)),
        ),
    ]