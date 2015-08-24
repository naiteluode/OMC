
#coding=utf-8
 
import urllib2, urllib, json, re
 
class SaltAPI(object):
    def __init__(self,url,username,password):
      #  self.__url = url.rstrip('/')
      #  self.__user =  username
      #  self.__password = password
        self.__url = 'https://127.0.0.1:8888'
        self.__user =  'saltapi'
        self.__password = 'saltapi'
        self.__token_id = self.salt_login()
 
    def salt_login(self):
        params = {'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        headers = {'X-Auth-Token':''}
        url = self.__url + '/login'
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError
 
    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        return content
        
    def list_all_key(self):
        params = {'client': 'wheel', 'fun': 'key.list_all'}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        minions = content['return'][0]['data']['return']['minions']
        minions_pre = content['return'][0]['data']['return']['minions_pre']
        return minions,minions_pre

    def delete_key(self,node_name):
        params = {'client': 'wheel', 'fun': 'key.delete', 'match': node_name}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def accept_key(self,node_name):
        params = {'client': 'wheel', 'fun': 'key.accept', 'match': node_name}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        ret = content['return'][0]['data']['success']
        return ret

    def remote_noarg_execution(self,tgt,fun):
        ''' Execute commands without parameters '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        ret = content['return'][0][tgt]
        return ret

    def remote_execution(self,tgt,fun,arg):
        ''' Command execution with parameters '''        
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg}
        obj = urllib.urlencode(params)
        #obj, number = re.subn("arg\d", 'arg', obj)
        #self.salt_login()
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret
    
    def remote_execution_noarg(self,tgt,fun):
        ''' Command execution with parameters '''        
        params = {'client': 'local', 'tgt': tgt, 'fun': fun}
        obj = urllib.urlencode(params)
        content = self.postRequest(obj)
        ret = content['return'][0]
        return ret

    def target_remote_execution(self,tgt,fun,arg):
        ''' Use targeting for remote execution '''
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'expr_form': 'nodegroup'}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        return jid

    def deploy(self,tgt,arg):
        ''' Module deployment '''
        params = {'client': 'local', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        return content

    def async_deploy(self,tgt,arg):
        ''' Asynchronously send a command to connected minions '''
        params = {'client': 'local_async', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        return jid

    def target_deploy(self,tgt,arg):
        ''' Based on the node group forms deployment '''
        params = {'client': 'local_async', 'tgt': tgt, 'fun': 'state.sls', 'arg': arg, 'expr_form': 'nodegroup'}
        obj = urllib.urlencode(params)
        #self.salt_login()
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        return jid 
    def saltCmd(self, params):
        obj = urllib.urlencode(params)
#        obj, number = re.subn("arg\d", 'arg', obj)
        res = self.postRequest(obj)
        return res
 
def main():
    #以下是用来测试saltAPI类的部分
    #sapi = saltAPI()
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'*'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'某台服务器的key'}
    #params = {'client':'local', 'fun':'test.echo', 'tgt':'某台服务器的key', 'arg1':'hello'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'某组服务器的组名', 'expr_form':'nodegroup'}
    #test = sapi.saltCmd(params)
    #print test
    pass
 
if __name__ == '__main__':
    main()