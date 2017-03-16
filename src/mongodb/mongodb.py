# coding:utf-8
'''
Created on 2017年3月16日
参考：http://blog.csdn.net/callinglove/article/details/45668673

@author: liucaiquan
'''
import pymongo
class MongoDB(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.ip = params
        self.port = 27017
        
    def init(self):
        # Connection
        self.con = pymongo.MongoClient(self.ip, self.port)
        # DB
        self.mydb = self.con['EddyDB']
        # Collection
        self.coll = self.mydb['EddyCollection']
        
    def insert(self, params):
        return self.coll.insert(params)
    
    def find(self, params):
        return self.coll.find_one(params)
        
        
        
        
