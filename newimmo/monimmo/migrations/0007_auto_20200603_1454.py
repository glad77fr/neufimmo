# Generated by Django 3.0.5 on 2020-06-03 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0006_programme_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programme',
            old_name='statut_livraison',
            new_name='statut',
        ),
    ]
