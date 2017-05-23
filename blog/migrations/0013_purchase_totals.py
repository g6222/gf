# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_purchase_free_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='totals',
            field=models.FloatField(default=0),
        ),
    ]
