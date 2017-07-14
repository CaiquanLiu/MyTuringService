# coding:utf-8
'''
Created on 2017年7月15日

@author: Administrator
'''
from baiduunit.unit import BaiduUnit
if __name__ == '__main__':
    unit=BaiduUnit()
#     print unit.get_token()

    query="深圳今天下雨吗"
    print unit.query_request(8218, query, "").text