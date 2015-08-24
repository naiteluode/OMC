# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.IPAddressField(unique=True)),
                ('osversion', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('disk', models.CharField(max_length=50)),
                ('vendor_id', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('cpu_core', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=50)),
                ('Manufacturer', models.CharField(max_length=50)),
                ('sn', models.CharField(max_length=50)),
                ('ping', models.CharField(max_length=50)),
                ('saltid', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Install',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.IPAddressField(unique=True)),
                ('product', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('osversion', models.CharField(max_length=50)),
                ('service', models.CharField(max_length=50)),
                ('ping', models.CharField(max_length=50)),
                ('progress', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='omcuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
