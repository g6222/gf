# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170519_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Free',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('goods_id', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
