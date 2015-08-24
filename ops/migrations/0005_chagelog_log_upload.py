# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0004_auto_20150521_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chagelog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltid', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('chage', models.CharField(max_length=255)),
                ('updatetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=50)),
                ('saltid', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('logtype', models.CharField(max_length=50)),
                ('cmd', models.CharField(max_length=255)),
                ('execerr', models.CharField(max_length=255)),
                ('logret', models.TextField(max_length=1000)),
                ('alter_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='./upload/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
