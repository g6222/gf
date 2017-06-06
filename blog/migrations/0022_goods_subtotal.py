# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_purchase_free_moeny'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='subtotal',
            field=models.FloatField(default=0),
        ),
    ]
