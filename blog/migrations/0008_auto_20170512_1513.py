# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20170512_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='goods_id',
            field=models.IntegerField(default=1),
        ),
    ]
