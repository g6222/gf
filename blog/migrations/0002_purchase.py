# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default='')),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
    ]
