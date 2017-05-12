# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170512_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='count',
            field=models.IntegerField(default=''),
        ),
    ]
