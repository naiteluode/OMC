#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render,render_to_response

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import admin
from django.contrib import auth
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import MySQLdb
from django.template.context import RequestContext
from omc import settings

##加载xlwt导出excel
import xlwt,StringIO
from xlwt import easyxf

#saltweb
import time,os,utils
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required 
from django.core.cache import cache
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt 
from django.views.decorators.csrf import csrf_protect 
import multiprocessing, threading
import salt
import base64
import csv
from ops.models import *
from ops.form import *
from ops.comm import *
import db_connector

# Import salt libs
import salt
import salt.client
import salt.config
import salt.utils
import salt.output
from salt._compat import string_types
from ops.saltapi import SaltAPI

#ansible api
import ansible.runner
from ansible.inventory import Inventory
import simplejson
import hashlib

# Create your views here.

def first(request):
	return render_to_response('first.html')
	
def index(request):
    return render_to_response('index.html')

def login(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = auth.authenticate(username=username,password=password)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/index/')
	else:
		return render_to_response('first.html',{'login_err':"Wrong Username or Password"})
	
def assets(request):
	Host_list = Host.objects.all()
	return render_to_response('assets.html',{'Host_list':Host_list})
	
def server(request):
	return render_to_response('server.html')

def install(request):
	Install_list = Install.objects.all()
	return render_to_response('install.html',{'Install_list':Install_list})
	
def log(request):
	return render_to_response('log.html')

def change(request):
    rets = Chagelog.objects.order_by("-updatetime")
    return render_to_response('changes.html',locals())

def filechange(request):
    rets = Chagelog.objects.order_by("-updatetime")
    return render_to_response('filechanges.html',locals())

def saltstack(request):
	return render_to_response('salt.html')
	
def ansible(request):
	return render_to_response('ansible.html')

def ansiblecmd(request):
	output = ''
	if request.method == 'POST':
		command = request.POST.get('command')
		output = os.popen(command).read()
	return render_to_response('ansible_cmd.html',{'output':output})

def file(request):
	return render_to_response('file.html')
	
def user(request):
	User_list = User.objects.all()
	return render_to_response('user.html',{'User_list':User_list})
	
def monitor(request):
	return render_to_response('monitor.html')
	
def test(req):
    print req
    if req.method == 'POST':
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osversion = req.POST.get('osversion')
        memory = req.POST.get('memory')
        disk = req.POST.get('disk')
        vendor_id = req.POST.get('vendor_id')
        model_name = req.POST.get('model_name')
        cpu_core = req.POST.get('cpu_core')
        product = req.POST.get('product')
        Manufacturer = req.POST.get('Manufacturer')
        sn = req.POST.get('sn')
        try:
            host = Hosts.objects.get(hostname=hostname)
        except:
            host = Host()
  
        host.hostname = hostname
        host.ip = ip
        host.osversion = osversion
        host.memory = memory
        host.disk = disk
        host.vendor_id = vendor_id
        host.model_name = model_name
        host.cpu_core = cpu_core
        host.product = product
        host.Manufacturer = Manufacturer
        host.sn = sn
        host.save()
  
        return render_to_response('test.html')
    else:
        return HttpResponse('no data')

def hostinfo(req):
    print req
    if req.method == 'POST':
        hostname = req.POST.get('hostname')
        ip = req.POST.get('ip')
        osversion = req.POST.get('osversion')
        memory = req.POST.get('memory')
        disk = req.POST.get('disk')
        vendor_id = req.POST.get('vendor_id')
        model_name = req.POST.get('model_name')
        cpu_core = req.POST.get('cpu_core')
        product = req.POST.get('product')
        Manufacturer = req.POST.get('Manufacturer')
        sn = req.POST.get('sn')
        try:
            host = Host.objects.get(hostname=hostname)
        except:
            host = Host()
  
        host.hostname = hostname
        host.ip = ip
        host.osversion = osversion
        host.memory = memory
        host.disk = disk
        host.vendor_id = vendor_id
        host.model_name = model_name
        host.cpu_core = cpu_core
        host.product = product
        host.Manufacturer = Manufacturer
        host.sn = sn
        host.save()
  
        return HttpResponse('ok')
    else:
        return HttpResponse('no data')

def assets_add(request):
    hostname = request.POST['hostname']
    ip = request.POST['ip']
    osversion = request.POST['osversion']
    memory = request.POST['memory']
    disk = request.POST['disk']
    vendor_id = request.POST['vendor_id']
    model_name = request.POST['model_name']
    cpu_core = request.POST['cpu_core']
    product = request.POST['product']
    Manufacturer = request.POST['Manufacturer']
    sn = request.POST['sn']
    ping = request.POST['ping']
    assets = Host()
    assets.hostname = hostname
    assets.ip = ip
    assets.osversion = osversion
    assets.memory = memory
    assets.disk = disk
    assets.vendor_id = vendor_id
    assets.model_name = model_name
    assets.cpu_core = cpu_core
    assets.product = product
    assets.Manufacturer = Manufacturer
    assets.sn = sn
    assets.ping = ping
    assets.save()
    return HttpResponseRedirect("/assets")
    
def exportassets(request):
    ## 创建book sheet
    workbook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workbook.add_sheet(u'资产清单')
    ##设置样式
    #font: bold on,colour_index green,height 360,family:Arial; 字体加粗，字体颜色，字体大小,字体类型
    #align: wrap on; 自动换行
    #pattern:fore_colour yellow, back_colour yellow，单元格的背景色，貌似要2个是一样的才生效
    #style_k = xlwt.easyxf('font:bold off,colour_index black,height 360;align:wrap on;borders:left 1,right 1,top 1,bottom 1;pattern:pattern alt_bars, fore_colour gray25, back_colour gray25')
    ##连接数据库
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='omc',port=3306)
    cur=conn.cursor()
    cur.execute('select * from ops_host')
    row_all = cur.fetchall()
    ##关闭数据库连接
    cur.close()
    conn.close()
    ##遍历表数据
    _lst = []  
    _lst.extend(row_all[:])          
    _lst.insert(0, ['序号','主机名', 'IP地址', '系统版本','CPU(核)','内存(G)','硬盘(G)','CPU品牌','CPU型号','品牌','SN','Ping','Saltid']) 
    ##数据写入sheet
    for row, rowdata in enumerate(_lst):  
        for col, val in enumerate(rowdata):  
            sheet.write(row, col, val, style=xlwt.Style.default_style) 
    ##定义Content-Disposition，让浏览器能识别，弹出下载框
    #解决ie不能下载的问题
    #excel 2007
    #response =HttpResponse(content_type="application/vnd.ms-excel")
    #excel 2003
    response =HttpResponse(content_type="application/ms-excel")
    #解决文件名乱码/不显示的问题
    response['Content-Disposition'] ='attachment; filename="export_assets.xls"'
    ##保存并下载
    workbook.save(response)
    return response
    
def saltcmd(request):
	return render_to_response('salt_cmd.html')
	
def saltminion(request):
    saltids = [row['saltid'] for row in Hosts.objects.values('saltid')]
    if request.method == 'POST':
        if request.POST.has_key("add"):
            port = sshdefaultport
            host = request.POST.get('host','')
            username = request.POST.get('username','')
            passwd = request.POST.get('passwd','')
            cmd = "Sys_ver=`uname -a|awk -F'el' '{print substr($2,1,1)}'` "
            cmd += '; [ $Sys_ver -eq 5 ] && sudo rpm -Uvh http://mirrors.sohu.com/fedora-epel/5/x86_64/epel-release-5-4.noarch.rpm \
                >/dev/null 2>&1'
            cmd += '; [ $Sys_ver -eq 6 ] && sudo rpm -Uvh http://mirrors.sohu.com/fedora-epel/6/x86_64/epel-release-6-8.noarch.rpm \
                >/dev/null 2>&1'
            cmd += '; sudo yum -y install salt-minion >/dev/null'
            cmd += '&& sudo sed -i "$ a\master: %s" /etc/salt/minion ' %masterip
            cmd += '&& sudo sed -i "$ a\id: %s_`hostname`" /etc/salt/minion ' % host
            cmd += '&& sudo /etc/init.d/salt-minion restart >/dev/null'
            cmd += "&& echo 'Success'"
            def sshfc():
                Monionslog.objects.create(name='add_minion',ip=host)
                id = Monionslog.objects.order_by('-id')[0].id
                ret = ssh(host,port,username,passwd,cmd)
                endtime = time.strftime("%Y-%m-%d %H:%M:%S")
                Monionslog.objects.filter(id=id).update(status='已完成',deployret=ret[host],endtime=endtime)
            threading.Thread(target=sshfc).start()
            time.sleep(1)   
        if request.POST.has_key("del"):
            saltid = request.POST.get('saltid','') 
            Monionslog.objects.create(name='del_minion',saltid=saltid)
            id = Monionslog.objects.order_by('-id')[0].id
            cmd = 'sed -i "s/^master/#master/g" /etc/salt/minion'
            cmd += '&& /etc/init.d/salt-minion stop >/dev/null'
            cmd += "&& echo 'Success'"
            c = salt.client.LocalClient()
            ret = c.cmd(saltid,'cmd.run',[cmd],timeout=5)
            if ret:
                ret = 'Success'
            else:
                ret = 'Error: minion 宕机或者salt-minion服务未开启'
            os.system('salt-key -d %s -y' % saltid )
            Hosts.objects.filter(saltid=saltid).delete()
            Monitor.objects.filter(saltid=saltid).delete()
            endtime = time.strftime("%Y-%m-%d %H:%M:%S")
            Monionslog.objects.filter(id=id).update(status='已完成',deployret=ret,endtime=endtime)
            Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='del_minion',execerr=ret)
    deployrets = Monionslog.objects.order_by('-id')[0:7]
    return render_to_response('salt_minion.html',locals())

def saltstatus(request):
    up = Monitor.objects.filter(saltstats='True').count()
    down = Monitor.objects.filter(saltstats='False').count()
    total = Monitor.objects.count() 
    ONE_PAGE_OF_DATA = pagelimit
    curPage = int(request.GET.get('curPage', '1'))
    allPage = int(request.GET.get('allPage','1'))
    pageType = str(request.GET.get('pageType', ''))
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    posts = Monitor.objects.order_by("saltstats")[startPos:endPos]
    if curPage == 1 and allPage == 1: 
        allPostCounts = Monitor.objects.count()
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
                allPage += 1
    id = request.GET.get('id',)
    closemail = request.GET.get('closemail',)
    Monitor.objects.filter(id=id).update(closemail=closemail)
    return render_to_response('salt_status.html',locals())

def saltstatus1(request):
	SaltHost_list = SaltHost.objects.all()
	paginator = Paginator(SaltHost_list,10)
	try:
	    page = int(request.GET.get('page','1'))
	except ValueError:
	    page = 1
	try:
	    SaltHost_list = paginator.page(page)
	except:
	    SaltHost_list = paginator.page(paginator.num_pages)
	return render_to_response('salt_status.html', {'SaltHost_list': SaltHost_list, 'page': page, 'paginator':paginator})

def saltdeploy(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    #ips = [row['ip'] for row in Hosts.objects.values('ip')]
    install_dir = upload_dir + 'saltdeploy'
    #files = os.listdir(install_dir)
    softs = [file for file in os.listdir(install_dir) if os.path.isfile("%s/%s" % (install_dir,file))]
    #softs = [row['soft'] for row in Soft.objects.values('soft')]
    if request.method == 'POST':
        if request.POST.has_key("saltdeploy"):
            saltid = request.POST.get('saltid','')
            software = request.POST.get('software','')
            cmd = "wget %s/saltdeploy/%s -O /tmp/%s >/dev/null 2>&1 && sh /tmp/%s >/dev/null 2>&1 && echo 'Install Success !!!'" % (download_url,software,software,software)
            def execcmd():
                c = salt.client.LocalClient()
                Deploylog.objects.create(name=software,saltid=saltid)
                id = Deploylog.objects.order_by('-id')[0].id
                rets = c.cmd(saltid,'cmd.run',[cmd],timeout=999)
                minions = c.run_job(saltid,'cmd.run',['echo'])['minions']
                retok = [ret[0] for ret in rets.items() if "Success" in ret[1]]
                execerr = list(set(minions).difference(set(retok)))
                total = len(minions)
                errnum = len(execerr)
                execerr = 'total:%d errnum:%d errret:%s' % (total,errnum,','.join(execerr))
                Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='install',cmd=cmd,execerr=execerr,logret=rets)
                endtime = time.strftime("%Y-%m-%d %H:%M:%S")
                Deploylog.objects.filter(id=id).update(status='已完成',deployret=execerr,endtime=endtime)
            threading.Thread(target=execcmd).start()
            time.sleep(1)
    deployrets = Deploylog.objects.order_by('-id')[0:7]
    return render_to_response('salt_deploy.html',locals())

def handle_uploaded_file(f): 
    f_path='./upload/'+f.name 
    with open(f_path, 'wb+') as info: 
        print f.name 
        for chunk in f.chunks(): 
            info.write(chunk) 
    return f 

def saltupload(request):
    downform = downfileForm(request.POST)
    class UploadFileForm(forms.Form): 
        title = forms.CharField(max_length=1000000) 
        file = forms.FileField() 
    if request.method == "POST":
        f = handle_uploaded_file(request.FILES['t_file'])
        ret = "文件上传成功!"
    if downform.is_valid():
	    filename = downform.cleaned_data['t_file'].strip()
	    File = upload_dir + filename
	    f = open(File)
	    data = f.read()
	    f.close()
	    response = HttpResponse(data,mimetype='application/octet-stream') 
	    response['Content-Disposition'] = 'attachment; filename=%s' % filename
	    return response
    else:
        ret = ''
    downform = downfileForm()
    uploaddir = upload_dir
    files = os.listdir(upload_dir)
    return render_to_response('salt_upload.html',locals()) 

def saltfile(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    files = [file for file in os.listdir(upload_dir) if os.path.isfile("%s/%s" % (upload_dir,file))]
    if request.method == 'POST':
        filename = request.POST.get('filename','')
        local = upload_dir + filename
        remote = request.POST.get('path','')
        saltid = request.POST.get('saltid','')
        cmd = 'wget %s%s -O %s >/dev/null 2>&1 && echo "Success push the files to target servers !"' % (download_url,filename,remote)
        c = salt.client.LocalClient()
        rets = c.cmd(saltid,'cmd.run',[cmd],timeout=5)
        minions = c.run_job(saltid,'cmd.run',['echo'])['minions']
        retok = [ret[0] for ret in rets.items() if "Success" in ret[1]]
        execerr = list(set(minions).difference(set(retok)))
        total = len(minions)
        errnum = len(execerr)
        execerr = 'total:%d errnum:%d errret:%s' % (total,errnum,','.join(execerr))
        Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='putfile',cmd=cmd,execerr=execerr,logret=rets)
    return render_to_response('salt_file.html', locals())

def saltgroup(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    if request.method == 'POST':
        groupname = request.POST['groupname']
        hosts = request.POST['hosts']
        if request.POST.has_key("add"):
            os.popen('echo "    %s: %s" >> %s' % (groupname,hosts,groupsconf))
        if request.POST.has_key("modf"):
            os.popen('sed -i "s/%s:.*/%s: %s/" %s' % (groupname,groupname,hosts,groupsconf))
        if request.POST.has_key("del"):
            os.popen('sed -i "/%s:.*/d" %s' % (groupname,groupsconf))
    #a = file(groupsconf).readlines()
    fp = open(groupsconf,'r')
    a = fp.readlines()
    fp.close()
    a.remove('nodegroups:\n')
    rets = {}
    for i in a:
        groupname = i.rstrip('\n').strip().split(':')[0]
        hosts = i.rstrip('\n').strip().split(':')[1]
        rets[groupname] = hosts
    return render_to_response('salt_group.html',locals())

def saltsysuser(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    users = [row.username for row in Users.objects.all()]
    if request.method == 'POST':
        if request.POST.has_key("adduser"):
            saltid = request.POST.get('saltid','')
            username = request.POST.get('username','')
            passwd = request.POST.get('passwd','')
            passwd1 = request.POST.get('passwd1','')
            usertype = request.POST.get('usertype','')
            if passwd == passwd1:
                cmd = "useradd %s >/dev/null 2>&1 &&echo %s|passwd --stdin %s >/dev/null 2>&1 &&echo 'successfully'" % (username,passwd,username)
                if usertype == '2':
                    cmd = '%s &&chattr -i /etc/sudoers && echo "%s  ALL=(ALL)  NOPASSWD: ALL">>/etc/sudoers && chattr +i /etc/sudoers' % (cmd,username)
                c = salt.client.LocalClient()
                minions = c.run_job(saltid,'cmd.run',['echo'])['minions']
                ret1 = c.cmd(saltid,'cmd.run',[cmd],timeout=5)
                retok = [ret[0] for ret in ret1.items() if "successfully" in ret[1]]
                execerr = list(set(minions).difference(set(retok)))
                total = len(minions)
                errnum = len(execerr)
                execerr = 'total:%d errnum:%d errret:%s' % (total,errnum,','.join(execerr))
                if username in users:
                    Users.objects.filter(username=username).update(passwd=passwd)
                else:
                    Users.objects.create(username=username,passwd=passwd)
                Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='adduser',cmd=cmd,execerr=execerr,logret=ret1)
            else:
                ret1 = {"two passwd do not match!!!":''}
        if request.POST.has_key("deluser"):
            saltid = request.POST.get('saltid','')
            username = request.POST.get('username','') 
            c = salt.client.LocalClient()
            minions = c.run_job(saltid,'cmd.run',['echo'])['minions'] 
            cmd = "userdel %s >/dev/null 2>&1 &&echo 'successfully'" % username
            ret1 = c.cmd(saltid,'cmd.run',[cmd],timeout=5)      
            print ret1    
            retok = [ret[0] for ret in ret1.items() if "successfully" in ret[1]]
            execerr = list(set(minions).difference(set(retok)))
            total = len(minions)
            errnum = len(execerr)
            execerr = 'total:%d errnum:%d errret:%s' % (total,errnum,','.join(execerr))
            if username in users:
                Users.objects.filter(username=username).delete()
            Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='deluser',cmd=cmd,execerr=execerr,logret=ret1)
        if request.POST.has_key("chpasswd"):
            saltid = request.POST.get('saltid','')
            username = request.POST.get('username','')
            passwd = request.POST.get('passwd','')
            passwd1 = request.POST.get('passwd1','')
            cmd = "echo %s|passwd --stdin %s" % (passwd,username)
            if passwd == passwd1:
                c = salt.client.LocalClient()
                minions = c.run_job(saltid,'cmd.run',['echo'])['minions']
                ret1 = c.cmd(saltid,'cmd.run',[cmd],timeout=5)
                retok = [ret[0] for ret in ret1.items() if "successfully" in ret[1]]
                execerr = list(set(minions).difference(set(retok)))
                total = len(minions)
                errnum = len(execerr)
                execerr = 'total:%d errnum:%d errret:%s' % (total,errnum,','.join(execerr))
                #if username == 'root':
                #    for i in ret1.keys():
                #        Hosts.objects.filter(saltid=i).update(passwd=passwd)
                if username in users:
                    Users.objects.filter(username=username).update(passwd=passwd)
                else:
                    Users.objects.create(username=username,passwd=passwd)
                Log.objects.create(user=str(user),ip='-',saltid=saltid,logtype='chpasswd',cmd=cmd,execerr=execerr,logret=ret1)
            else:
                ret1 = {"two passwd do not match!!!":''}
    return render_to_response('salt_sysuser.html', locals())

def saltlog(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    ONE_PAGE_OF_DATA = pagelimit
    curPage = int(request.GET.get('curPage', '1'))
    allPage = int(request.GET.get('allPage','1'))
    pageType = str(request.GET.get('pageType', ''))
    if pageType == 'pageDown':
        curPage += 1
    elif pageType == 'pageUp':
        curPage -= 1

    startPos = (curPage - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    #posts = Log.objects.filter(user=user).order_by('-alter_time')[startPos:endPos]
    posts = Log.objects.order_by('-alter_time')[startPos:endPos]
    if curPage == 1 and allPage == 1: 
        #allPostCounts = Log.objects.filter(user=user).count()
        allPostCounts = Log.objects.count()
        allPage = allPostCounts / ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
                allPage += 1
    return render_to_response('salt_log.html', locals())

def remote_execution(request):
    ret = ''
    tret = ''
    dangerCmd = ('rm','reboot','init','shutdown','poweroff')
    if request.method == 'POST':
        action = request.get_full_path().split('=')[1]
        if action == 'exec':
            tgt = request.POST.get('tgt','')
            fun = request.POST.get('fun','')
            arg = request.POST.get('arg','')    
        if tgt:
            if fun:
                if arg:
                    argCmd = arg.split()[0]
                    argCheck = argCmd not in dangerCmd
                    if argCheck:
                        sapi = SaltAPI(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password'])
                        unret = sapi.remote_execution(tgt,fun,arg)
                        for kret in unret.keys():
                            lret = kret + ':\n' + unret[kret] + '\n'
                            tret += lret + '\n'
                        ret = tret
                    elif not argCheck:
                        ret = '危险命令，不允许执行！'
                else:
                    ret = '没有输入命令，请重新输入！'
            else:
                ret = '未指定执行模块，请重新输入！'
        else:
            ret = '未指定目标主机，请重新输入！'
         
    return render_to_response('salt_cmd.html',{'ret': ret},context_instance=RequestContext(request)) 
    
def ansiblegroup(request):
    #user = request.user
    #msgnum = Msg.objects.filter(isread=0,msgto=user).count()
    if request.method == 'POST':
        groupname = request.POST['groupname']
        hosts = request.POST['hosts']
        if request.POST.has_key("add"):
            os.popen('sudo echo -e "[%s]\n %s" >> %s' % (groupname,hosts,ansiblegroupsconf))
        if request.POST.has_key("modf"):
            os.popen('sudo sed -i "s/[%s]/%s/" %s' % (groupname,groupname,ansiblegroupsconf))
            os.popen('sudo sed -i "s/%s/%s/" %s' % (hosts,hosts,ansiblegroupsconf))
        if request.POST.has_key("del"):
            os.popen('sudo sed -i "/[%s]/d" %s' % (groupname,ansiblegroupsconf))
    #a = file(groupsconf).readlines()
    fp = open(ansiblegroupsconf,'r')
    a = fp.readlines()
    fp.close()
    #a.remove('nodegroups:\n')
    rets = {}
    for i in a:
        groupname = i.rstrip('[]')[0]
        hosts = i.rstrip('\n')
        rets[groupname] = hosts
    return render_to_response('ansible_group.html',locals())
