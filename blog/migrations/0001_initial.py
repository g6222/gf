# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField(default='')),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
    ]
