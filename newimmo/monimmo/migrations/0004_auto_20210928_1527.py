# Generated by Django 3.0.5 on 2021-09-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0003_post_subject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='content',
            field=models.TextField(blank=True, max_length=1500, null=True),
        ),
    ]