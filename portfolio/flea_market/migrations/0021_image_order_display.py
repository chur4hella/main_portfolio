# Generated by Django 3.2.6 on 2021-11-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0020_auto_20211105_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='order_display',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
