# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_purchase_free_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='free_moeny',
            field=models.FloatField(default=0),
        ),
    ]
