# Generated by Django 3.0.5 on 2020-10-01 15:31

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monimmo', '0015_auto_20200626_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(blank=True, max_length=1500, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, blank=True, editable=True, max_length=255, populate_from='content')),
            ],
        ),
    ]
