from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

from django.db import models
from django.contrib.auth.views import login, logout
from ops.views import *
from django.contrib import admin
admin.autodiscover()
#import xadmin
#xadmin.autodiscover()
#from xadmin.plugins import xversion
#xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'omc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^xadmin/', include(xadmin.site.urls)),
    url(r'^$', 'ops.views.first'),
    url(r'^index/$', 'ops.views.index'),
    #url(r'^login/$', 'ops.views.login'),
    url(r'^assets/$', 'ops.views.assets'),
    url(r'^assets_add/$', 'ops.views.assets_add'),
    url(r'^exportassets/$', 'ops.views.exportassets'),
    url(r'^server/$', 'ops.views.server'),
    url(r'^install/$', 'ops.views.install'),
    url(r'^log/$', 'ops.views.log'),
    url(r'^user/$', 'ops.views.user'),
    url(r'^change/$', 'ops.views.change'),
    url(r'^filechange/$', 'ops.views.filechange'),
    url(r'^salt/$', 'ops.views.saltstack'),
    url(r'^saltcmd/$','ops.views.saltcmd'),
    url(r'^remote_execution/$','ops.views.remote_execution'),
    url(r'^saltminion/$','ops.views.saltminion'),
    url(r'^saltstatus/$','ops.views.saltstatus'),
    url(r'^saltdeploy/$','ops.views.saltdeploy'),
    url(r'^saltupload/$','ops.views.saltupload'),
    url(r'^saltfile/$','ops.views.saltfile'),
    url(r'^saltgroup/$','ops.views.saltgroup'),
    url(r'^saltsysuser/$','ops.views.saltsysuser'),
    url(r'^saltlog/$','ops.views.saltlog'),
    url(r'^file/$', 'ops.views.file'),
    url(r'^monitor/$','ops.views.monitor'),
    url(r'^test/$','ops.views.test'),
    url(r'^hostinfo/$','ops.views.hostinfo'),
    url(r'^ansible/$','ops.views.ansible'),
    url(r'^ansiblecmd/$','ops.views.ansiblecmd'),
    url(r'^ansiblegroup/$','ops.views.ansiblegroup'),
)
