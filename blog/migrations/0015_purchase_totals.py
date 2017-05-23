# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_purchase_totals'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='totals',
            field=models.FloatField(default=0),
        ),
    ]
