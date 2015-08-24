# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=15, verbose_name='IP\u5730\u5740', blank=True)),
                ('macaddr', models.CharField(max_length=20, verbose_name='MAC\u5730\u5740', blank=True)),
                ('licdate', models.CharField(max_length=30, verbose_name='\u6388\u6743\u65e5\u671f', blank=True)),
                ('licstatus', models.CharField(max_length=30, verbose_name='\u6388\u6743\u72b6\u6001', blank=True)),
                ('remark', models.TextField(max_length=200, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
