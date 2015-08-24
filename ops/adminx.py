#coding=utf-8
from django.contrib import admin

from ops.models import *

# Register your models here.
#新增资产清单表
class HostAdmin(admin.ModelAdmin):
    search_fields = ('id','ip')
    list_display = [
                'hostname',
                'osversion',
                'memory',
                'disk',
                'vendor_id',
                'model_name',
                'cpu_core',
                'product',
                'Manufacturer',
                'sn',
                'ping']
 
xadmin.site.register(Host,HostAdmin)

#新增装机清单表
class InstallAdmin(admin.ModelAdmin):
    search_fields = ('id','ip')
    list_display = [
                'ip',
                'product',
                'place',
                'osversion',
                'service',
                'ping',
                'progress']
 
xadmin.site.register(Install,InstallAdmin)

xadmin.site.register(omcuser)

class SaltHostAdmin(admin.ModelAdmin):
    search_fields = ('id','ip')
    list_display = [
                'ip',
                'serverstatus',
                'saltstatus',
                'alarmstatus',
                'licdate',
                'licstatus',
                'operation']
 
xadmin.site.register(SaltHost,SaltHostAdmin)

#### Saltweb  ####
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

xadmin.site.register(Pro_type)
xadmin.site.register(Users,UsersAdmin)
xadmin.site.register(Hosts,HostsAdmin)
xadmin.site.register(Monitor,MonitorAdmin)
xadmin.site.register(Mastermonitor,MastermonitorAdmin)
xadmin.site.register(Upload,UploadAdmin)
xadmin.site.register(Log,LogAdmin)
xadmin.site.register(Soft)
xadmin.site.register(Monitortype,MonitortypeAdmin)
xadmin.site.register(Chagelog,ChagelogAdmin)
xadmin.site.register(Address)
xadmin.site.register(Msg,MsgAdmin)
xadmin.site.register(Url)
xadmin.site.register(Deploylog,DeploylogAdmin)
xadmin.site.register(Alarm,AlarmAdmin)
xadmin.site.register(Monionslog,MonionslogAdmin)
