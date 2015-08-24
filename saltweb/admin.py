#!/usr/bin/env python
#coding=utf-8
#author: hhr
from django.contrib import admin
from saltweb.models import *

class HostsAdmin(admin.ModelAdmin):
    list_display = ('saltid','ip','hostname','host_type','mem','os','sn','model','disk','update_date','mark')
    ordering = ('update_date',)
    search_fields = ('saltid', 'hostname')
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username','passwd')
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('saltid','ip','pingstats','saltstats','load','connum','num','nowtime','sendmail','closemail')
    ordering = ('saltstats',)
class MastermonitorAdmin(admin.ModelAdmin):
    list_display = ('saltid','ip','connum','num','nowtime','sendmail','closemail')
class UploadAdmin(admin.ModelAdmin):
    list_display = ('name','file')
class LogAdmin(admin.ModelAdmin):
    list_display = ('user','saltid','ip','logtype','cmd','execerr','logret','alter_time')
    ordering = ('-alter_time',)

class MonitortypeAdmin(admin.ModelAdmin):
    list_display = ('name','alias')
class ChagelogAdmin(admin.ModelAdmin):
    list_display = ('saltid','ip','chage','updatetime')
class MsgAdmin(admin.ModelAdmin):
    list_display = ('msgfrom','msgto','title','content','isread','pubtime')
    ordering = ('-pubtime',)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('proname','domainname','ip','prot','url','pubtime','state')
    ordering = ('-pubtime',)
class DeploylogAdmin(admin.ModelAdmin):
    list_display = ('name','saltid','ip','starttime','status','deployret','endtime')
    ordering = ('-id',)
class AlarmAdmin(admin.ModelAdmin):
    list_display = ('hostid','msg','to','nowtime')
    ordering = ('-id',)
class MonionslogAdmin(admin.ModelAdmin):
    list_display = ('name','saltid','ip','starttime','status','deployret','endtime')
    ordering = ('-id',)

admin.site.register(Pro_type)
admin.site.register(Users,UsersAdmin)
admin.site.register(Hosts,HostsAdmin)
admin.site.register(Monitor,MonitorAdmin)
admin.site.register(Mastermonitor,MastermonitorAdmin)
admin.site.register(Upload,UploadAdmin)
admin.site.register(Log,LogAdmin)
admin.site.register(Soft)
admin.site.register(Monitortype,MonitortypeAdmin)
admin.site.register(Chagelog,ChagelogAdmin)
admin.site.register(Address)
admin.site.register(Msg,MsgAdmin)
admin.site.register(Url)
admin.site.register(Deploylog,DeploylogAdmin)
admin.site.register(Alarm,AlarmAdmin)
admin.site.register(Monionslog,MonionslogAdmin)
