#coding:utf-8
'''
Created on 2017年3月16日

@author: liucaiquan
'''
from turing.turing import Turing
if __name__ == '__main__':
    turing = Turing()
    response = turing.request("今天天气怎么样呀？")
    print response.text