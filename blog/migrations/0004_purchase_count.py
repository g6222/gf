# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_purchase_goods_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='count',
            field=models.DecimalField(decimal_places=0, max_digits=100, default=0),
        ),
    ]
