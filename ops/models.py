#!/usr/bin/env python
#coding=utf-8
from __future__ import unicode_literals
from django.db import models

from django.db.models import *
from django.contrib.auth.models import User
from ops.comm import *

from django.contrib import admin

# Create your models here.
class omcuser(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    def __unicode__(self):
        return self.username

class Host(models.Model):
    hostname = models.CharField(max_length=50,  blank=True,verbose_name=u'主机名')
    ip = models.IPAddressField(unique=True,  blank=True,verbose_name=u'IP地址')
    osversion = models.CharField(max_length=50,  blank=True,verbose_name=u'系统版本')
    memory = models.CharField(max_length=50,  blank=True,verbose_name=u'内存')
    disk = models.CharField(max_length=50,  blank=True,verbose_name=u'硬盘')
    vendor_id = models.CharField(max_length=50,  blank=True,verbose_name=u'CPUvendor')
    model_name = models.CharField(max_length=50,  blank=True,verbose_name=u'CPUmodel')
    cpu_core = models.CharField(max_length=50,  blank=True,verbose_name=u'CPU核数')
    product = models.CharField(max_length=50,  blank=True,verbose_name=u'品牌')
    Manufacturer = models.CharField(max_length=50,  blank=True,verbose_name=u'Manufacturer')
    sn = models.CharField(max_length=50,  blank=True,verbose_name=u'SN号')
    ping = models.CharField(max_length=50,  blank=True,verbose_name=u'能否Ping通')
    saltid = models.CharField(max_length=50,  blank=True,verbose_name=u'SaltID')
    
    def __unicode__(self):
        return self.ip
    
class Install(models.Model):
    ip = models.IPAddressField(unique=True)
    product = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    osversion = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    ping = models.CharField(max_length=50)
    progress = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.ip

class SaltHost(models.Model):
    ip = models.CharField(max_length=15,  blank=True,verbose_name=u'IP地址')
    serverstatus = models.CharField(max_length=30,  blank=True,verbose_name=u'主机状态')
    saltstatus = models.CharField(max_length=30,  blank=True,verbose_name=u'Salt状态')
    alarmstatus = models.CharField(max_length=30,  blank=True,verbose_name=u'报警状态')
    licdate = models.CharField(max_length=30,  blank=True,verbose_name=u'授权日期')
    licstatus = models.CharField(max_length=30, blank=True, verbose_name=u'授权状态')
    operation = models.TextField(max_length=200, blank=True, verbose_name=u'操作')

    def __unicode__(self):
        return self.ip


#### Saltweb ####
class Pro_type(Model):
    _database = 'salt'
    name = CharField(max_length=50,default='SSH')
    def __unicode__(self):
        return self.name

#非root账号密码表，所有服务器账号密码统一
class Users(Model):
    _database = 'salt'
    username = CharField(max_length=50,default='hhr')
    passwd = CharField(max_length=50,default='123')
    #protocol_type = ForeignKey(Pro_type)
    #pkey_file = CharField(max_length=50,default='/home/hhr/.ssh/id_rsa')
class Hosts(Model):
    _database = 'salt'
    saltid = CharField(max_length=50)
    hostname = CharField(max_length=50)
    ip = IPAddressField(unique=True)
    host_type = CharField(max_length=50,default='虚拟机')
    user = CharField(max_length=50,default='root')
    passwd = CharField(max_length=50,default='123')
    mem = CharField(max_length=50)
    os = CharField(max_length=50)
    port = IntegerField(default=sshdefaultport)
    #protocol_type = ForeignKey(Pro_type)
    cpu = CharField(max_length=50,blank=True)
    cpunum = IntegerField()
    model = CharField(max_length=50,default='Null')
    sn = CharField(max_length=50,default='Null')
    disk = CharField(max_length=50,default='Null')
    mark = CharField(max_length=100,blank=True)
    update_date = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.ip

class Monitor(Model):
    _database = 'salt'
    saltid = CharField(max_length=50)
    ip = IPAddressField()
    pingstats = CharField(max_length=10,blank=True)
    saltstats = CharField(max_length=10,blank=True)
    load = CharField(max_length=50,blank=True)
    connum = CharField(max_length=100,blank=True)
    num = IntegerField(default=0)
    nowtime = CharField(max_length=100,blank=True)
    sendmail = IntegerField(default=0)
    closemail = IntegerField(default=0)
    def __unicode__(self):
        return self.saltid

class Mastermonitor(Model):
    _database = 'salt'
    saltid = CharField(max_length=50,default='saltwebmaster')
    ip = IPAddressField()
    #pingstats = CharField(max_length=10,blank=True)
    #saltstats = CharField(max_length=10,blank=True)
    #load = CharField(max_length=50,blank=True)
    connum = CharField(max_length=100,blank=True)
    num = IntegerField(default=0)
    nowtime = CharField(max_length=100,blank=True)
    sendmail = IntegerField(default=0)
    closemail = IntegerField(default=0)
    def __unicode__(self):
        return self.saltid

class Upload(Model):
    _database = 'salt'
    name = CharField(max_length=100)
    file = FileField(upload_to="./upload/");
    def __unicode__(self):
        return self.name

class Log(Model):
    _database = 'salt'
    user = CharField(max_length=50)
    saltid = CharField(max_length=50)
    ip = CharField(max_length=50)
    logtype = CharField(max_length=50)
    cmd = CharField(max_length=255)
    execerr = CharField(max_length=255)
    logret = TextField(max_length=1000)
    alter_time = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.saltid

class Soft(Model):
    _database = 'salt'
    soft = CharField(max_length=50)
    def __unicode__(self):
        return self.soft

class Monitortype(Model):
    _database = 'salt'
    name = CharField(max_length=50)
    alias = CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Chagelog(Model):
    _database = 'salt'
    saltid = CharField(max_length=50)
    ip = CharField(max_length=50)
    chage = CharField(max_length=255)
    updatetime = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.saltid

class Address(Model): 
    _database = 'salt'
    name = CharField("姓名",max_length=32,unique=True) 
    gender = CharField("性别",choices=(("M","男"),("F","女")),max_length=1) 
    #telphone = CharField("电话",max_length=20) 
    mobile = CharField("手机",max_length=11) 
    room = CharField('房间', max_length=32) 
    def __unicode__(self): 
        return self.name 
        
class Msg(Model):
    _database = 'salt'
    msgfrom = CharField(max_length=50)
    msgto = CharField(max_length=50)
    title = CharField(max_length=50)
    content = TextField(max_length=500)
    pubtime = DateTimeField(auto_now_add=True)
    isread = IntegerField(default=0)
    def __unicode__(self):
        return self.title
        
class Url(Model):
    _database = 'salt'
    proname = CharField(max_length=50,unique=True)
    domainname = CharField(max_length=50)
    ip = CharField(max_length=50)
    port = IntegerField()
    urlname = CharField(max_length=100)
    pubtime = DateTimeField(auto_now_add=True)
    state = CharField(max_length=10)
    def __unicode__(self):
        return self.proname

class Deploylog(Model):
    _database = 'salt'
    name = CharField(max_length=50)
    ip = CharField(max_length=50)
    saltid = CharField(max_length=50)
    status = CharField(max_length=50,default='进行中')
    deployret = CharField(max_length=500)
    starttime = DateTimeField(auto_now_add=True)
    endtime = CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Monionslog(Model):
    _database = 'salt'
    name = CharField(max_length=50)
    ip = CharField(max_length=50)
    saltid = CharField(max_length=50)
    status = CharField(max_length=50,default='进行中')
    deployret = CharField(max_length=500)
    starttime = DateTimeField(auto_now_add=True)
    endtime = CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Alarm(Model):
    _database = 'salt'
    hostid = CharField(max_length=50)
    msg = CharField(max_length=500)
    to = CharField(max_length=50)
    nowtime = DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.hostid
