# Generated by Django 3.0.5 on 2020-06-01 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0003_auto_20200601_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='date_livraison_act',
            field=models.DateField(blank=True, null=True, verbose_name='Date de livraison prévue'),
        ),
    ]
