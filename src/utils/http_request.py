# coding:utf-8
'''
Created on 2017年3月7日
参考：https://my.oschina.net/yangyanxing/blog/280029

@author: liucaiquan
'''
import requests

class HttpRequest(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.url = params
        
    def get(self, params):    
        return requests.get(self.url, params=params)
    
    def post(self, params):
        return requests.post(self.url, data=params)
        
        
        
        
        
    
