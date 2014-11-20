# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='kid',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
