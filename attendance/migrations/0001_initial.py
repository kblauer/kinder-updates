# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attDate', models.DateField()),
                ('didAtt', models.BooleanField(default=False)),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('kid', models.ForeignKey(to='kids.Kid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
