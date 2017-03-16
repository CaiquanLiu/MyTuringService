#coding:utf-8
'''
Created on 2017年3月16日

@author: liucaiquan
'''
from utils.word_seg_finalseg import Finalseg
if __name__ == '__main__':
    seg=Finalseg()
    sentence="请给我讲一个故事"
    rst=seg.cut(sentence)
    print "/ ".join(rst)