# coding:utf-8
'''
Created on 2017年3月7日

@author: liucaiquan
'''
from utils.http_request import HttpRequest
import json

class Turing(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.key = "key"
        self.key_value = "5e3c2b7eb5bb42caad216d02cde38920"
        self.info = "info"
        self.http_request = HttpRequest("http://www.tuling123.com/openapi/api")
        
    def request(self, params):
        data = {self.key:self.key_value, self.info:params}
        return self.http_request.post(json.dumps(data))
        
        
