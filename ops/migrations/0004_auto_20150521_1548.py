# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0003_auto_20150521_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='Manufacturer',
            field=models.CharField(max_length=50, verbose_name='Manufacturer', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='cpu_core',
            field=models.CharField(max_length=50, verbose_name='CPU\u6838\u6570', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='disk',
            field=models.CharField(max_length=50, verbose_name='\u786c\u76d8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(max_length=50, verbose_name='\u4e3b\u673a\u540d', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=models.IPAddressField(unique=True, verbose_name='IP\u5730\u5740', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='memory',
            field=models.CharField(max_length=50, verbose_name='\u5185\u5b58', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='model_name',
            field=models.CharField(max_length=50, verbose_name='CPUmodel', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='osversion',
            field=models.CharField(max_length=50, verbose_name='\u7cfb\u7edf\u7248\u672c', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='ping',
            field=models.CharField(max_length=50, verbose_name='\u80fd\u5426Ping\u901a', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='product',
            field=models.CharField(max_length=50, verbose_name='\u54c1\u724c', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='saltid',
            field=models.CharField(max_length=50, verbose_name='SaltID', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='sn',
            field=models.CharField(max_length=50, verbose_name='SN\u53f7', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='host',
            name='vendor_id',
            field=models.CharField(max_length=50, verbose_name='CPUvendor', blank=True),
            preserve_default=True,
        ),
    ]
