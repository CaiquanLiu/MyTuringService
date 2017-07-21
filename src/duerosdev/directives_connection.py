# coding:utf-8
'''
Created on 2017年7月19日
通过Http/2 get的方式同DuerOS后台服务建立长链接
@author: liucaiquan
'''
from hyper import HTTP20Connection
from common_params import host, authorization, dueros_device_id, path_get_directives
class DriectivesLongConnection(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.val_authorization=authorization
        self.val_dueros_device_id=dueros_device_id
        
        self.val_host=host
        self.val_path=path_get_directives
        
        self.conn = HTTP20Connection(self.val_host)
        
        self.headers={'authorization':self.val_authorization, \
         'dueros-device-id':self.val_dueros_device_id}
        
    def get(self):
        self.conn.request('GET', self.val_path, headers=self.headers)
        resp = self.conn.get_response()
        return resp.read()
        
        