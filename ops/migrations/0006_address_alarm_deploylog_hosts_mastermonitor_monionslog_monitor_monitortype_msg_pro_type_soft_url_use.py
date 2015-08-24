# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0005_chagelog_log_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name='\u59d3\u540d')),
                ('gender', models.CharField(max_length=1, verbose_name='\u6027\u522b', choices=[('M', '\u7537'), ('F', '\u5973')])),
                ('mobile', models.CharField(max_length=11, verbose_name='\u624b\u673a')),
                ('room', models.CharField(max_length=32, verbose_name='\u623f\u95f4')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostid', models.CharField(max_length=50)),
                ('msg', models.CharField(max_length=500)),
                ('to', models.CharField(max_length=50)),
                ('nowtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Deploylog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('saltid', models.CharField(max_length=50)),
                ('status', models.CharField(default='\u8fdb\u884c\u4e2d', max_length=50)),
                ('deployret', models.CharField(max_length=500)),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltid', models.CharField(max_length=50)),
                ('hostname', models.CharField(max_length=50)),
                ('ip', models.IPAddressField(unique=True)),
                ('host_type', models.CharField(default='\u865a\u62df\u673a', max_length=50)),
                ('user', models.CharField(default='root', max_length=50)),
                ('passwd', models.CharField(default='123', max_length=50)),
                ('mem', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('port', models.IntegerField(default=50718)),
                ('cpu', models.CharField(max_length=50, blank=True)),
                ('cpunum', models.IntegerField()),
                ('model', models.CharField(default='Null', max_length=50)),
                ('sn', models.CharField(default='Null', max_length=50)),
                ('disk', models.CharField(default='Null', max_length=50)),
                ('mark', models.CharField(max_length=100, blank=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mastermonitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltid', models.CharField(default='saltwebmaster', max_length=50)),
                ('ip', models.IPAddressField()),
                ('connum', models.CharField(max_length=100, blank=True)),
                ('num', models.IntegerField(default=0)),
                ('nowtime', models.CharField(max_length=100, blank=True)),
                ('sendmail', models.IntegerField(default=0)),
                ('closemail', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Monionslog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('saltid', models.CharField(max_length=50)),
                ('status', models.CharField(default='\u8fdb\u884c\u4e2d', max_length=50)),
                ('deployret', models.CharField(max_length=500)),
                ('starttime', models.DateTimeField(auto_now_add=True)),
                ('endtime', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saltid', models.CharField(max_length=50)),
                ('ip', models.IPAddressField()),
                ('pingstats', models.CharField(max_length=10, blank=True)),
                ('saltstats', models.CharField(max_length=10, blank=True)),
                ('load', models.CharField(max_length=50, blank=True)),
                ('connum', models.CharField(max_length=100, blank=True)),
                ('num', models.IntegerField(default=0)),
                ('nowtime', models.CharField(max_length=100, blank=True)),
                ('sendmail', models.IntegerField(default=0)),
                ('closemail', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Monitortype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msgfrom', models.CharField(max_length=50)),
                ('msgto', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('pubtime', models.DateTimeField(auto_now_add=True)),
                ('isread', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pro_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='SSH', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('soft', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proname', models.CharField(unique=True, max_length=50)),
                ('domainname', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('urlname', models.CharField(max_length=100)),
                ('pubtime', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default='hhr', max_length=50)),
                ('passwd', models.CharField(default='123', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
