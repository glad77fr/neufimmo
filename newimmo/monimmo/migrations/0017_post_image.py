# Generated by Django 3.0.5 on 2022-04-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0016_auto_20220421_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]