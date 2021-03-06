# Generated by Django 3.2.6 on 2021-10-12 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flea_market', '0008_alter_ad_date_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('parent_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='flea_market.region')),
            ],
        ),
    ]
