# Generated by Django 3.0.5 on 2020-06-01 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0002_auto_20200502_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programme',
            name='date_livraison_act',
            field=models.DateField(blank=True, verbose_name='Date de livraison prévue'),
        ),
        migrations.AlterField(
            model_name='programme',
            name='statut_livraison',
            field=models.IntegerField(choices=[(1, 'En commercialisation'), (2, 'En construction'), (3, 'Terminé')]),
        ),
    ]
