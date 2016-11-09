# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='count',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('database_name', models.CharField(max_length=20)),
                ('table_name', models.CharField(max_length=20)),
                ('tag_name', models.CharField(max_length=20)),
                ('num', models.IntegerField(default=0)),
                ('pub_time', models.DateTimeField()),
                ('create_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
