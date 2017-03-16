# coding:utf-8
'''
Created on 2017年3月14日

@author: liucaiquan
'''
import finalseg
class Finalseg(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def cut(self, sentence):
        cut_rst = finalseg.cut(sentence)
        return "/ ".join(cut_rst)
        
