# Generated by Django 3.2.6 on 2021-10-29 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0014_alter_ad_type_ad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='type_ad',
            field=models.CharField(choices=[('buy', 'Куплю'), ('sell', 'Продам'), ('exchange', 'Обмен'), ('service', 'Услуга'), ('rent', 'Аренда')], default=('buy', 'Куплю'), max_length=15, verbose_name='Тип объявления'),
        ),
    ]