#coding:utf-8
'''
Created on 2017年3月16日

@author: liucaiquan
'''
from mongodb.mongodb import MongoDB
if __name__ == '__main__':
    db = MongoDB("127.0.0.1")
     
    db.init()
     
    infor1 = {"name": "eddy", "age": 31}
    infor2 = {"name":"cissy", "age":26}
     
    db.insert(infor1)
    db.insert(infor2)
     
    print db.find({"name":"eddy"})
