# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_remove_purchase_totals'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
