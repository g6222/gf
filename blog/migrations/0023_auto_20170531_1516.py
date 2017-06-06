# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_goods_subtotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='free_counts',
            field=models.FloatField(default=0),
        ),
    ]
