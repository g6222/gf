# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_free_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='free',
            field=models.IntegerField(default=0),
        ),
    ]
