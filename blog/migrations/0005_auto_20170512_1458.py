# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_purchase_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='count',
            field=models.FloatField(default=''),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='goods_id',
            field=models.FloatField(default=''),
        ),
    ]
