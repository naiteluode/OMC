# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0002_hostlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaltHost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=15, verbose_name='IP\u5730\u5740', blank=True)),
                ('serverstatus', models.CharField(max_length=30, verbose_name='\u4e3b\u673a\u72b6\u6001', blank=True)),
                ('saltstatus', models.CharField(max_length=30, verbose_name='Salt\u72b6\u6001', blank=True)),
                ('alarmstatus', models.CharField(max_length=30, verbose_name='\u62a5\u8b66\u72b6\u6001', blank=True)),
                ('licdate', models.CharField(max_length=30, verbose_name='\u6388\u6743\u65e5\u671f', blank=True)),
                ('licstatus', models.CharField(max_length=30, verbose_name='\u6388\u6743\u72b6\u6001', blank=True)),
                ('operation', models.TextField(max_length=200, verbose_name='\u64cd\u4f5c', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='HostList',
        ),
    ]
