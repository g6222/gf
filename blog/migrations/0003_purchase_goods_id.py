# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='goods_id',
            field=models.DecimalField(max_digits=100, decimal_places=0, default=0),
        ),
    ]
