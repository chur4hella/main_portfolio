# Generated by Django 3.2.6 on 2021-11-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0021_image_order_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='flea_market/uploads/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]