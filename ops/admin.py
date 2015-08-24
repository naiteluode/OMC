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
 
admin.site.register(Host,HostAdmin)

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
 
admin.site.register(Install,InstallAdmin)

admin.site.register(omcuser)

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
 
admin.site.register(SaltHost,SaltHostAdmin)

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