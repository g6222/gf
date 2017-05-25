# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_goods_free'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='free',
            field=models.IntegerField(default=0),
        ),
    ]
