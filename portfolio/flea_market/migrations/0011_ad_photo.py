# Generated by Django 3.2.6 on 2021-10-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0010_ad_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
