# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_purchase_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='free_count',
            field=models.IntegerField(default=0),
        ),
    ]
