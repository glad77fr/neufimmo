# Generated by Django 3.0.5 on 2022-04-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0018_auto_20220425_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='subject',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
