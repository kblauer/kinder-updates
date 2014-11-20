# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0002_auto_20141028_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedbackText', models.TextField()),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('parentId', models.ForeignKey(to='updates.Update')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
