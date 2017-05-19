# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170519_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
    ]
