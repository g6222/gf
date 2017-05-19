# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170512_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='subtotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='goods_id',
            field=models.IntegerField(default=0),
        ),
    ]
