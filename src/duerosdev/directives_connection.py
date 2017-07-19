# coding:utf-8
'''
Created on 2017年7月19日

@author: liucaiquan
'''
from hyper import HTTP20Connection
class DriectivesConnection(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.val_bearer="Bearer "#注意空格
        # 临时使用度秘”AI小助手“的Token
        self.val_token="23.027c7321a14bdbf673adc59b154b43b1.2592000.1502956721.2550887388-9874433"
        self.val_authorization=self.val_bearer+self.val_token
        # 临时使用小米5S测试机的DeviceID
        self.val_dueros_device_id="ffffffff-e76f-1bdf-0000-000063ec21a0"
        
        self.val_host="dueros-h2.baidu.com"
        self.val_path="/dcs/v1/directives"
        
        self.conn = HTTP20Connection(self.val_host)
        
        self.headers={'authorization':self.val_authorization, \
         'dueros-device-id':self.val_dueros_device_id}
        
    def get(self):
        self.conn.request('GET', self.val_path, headers=self.headers)
        resp = self.conn.get_response()
        return resp.read()
        
        