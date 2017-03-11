# coding:utf-8
import requests
import json
import common_params
 
requestData = {common_params.KEY_REQUEST_TYPE:common_params.REQUEST_TYPE_TURING, common_params.REQUEST_TURING_CONTENT:'今天百度股票怎么样？'}
 
# print requestData
    
r = requests.post('http://' + common_params.HTTP_SERVER_IP + ':' + common_params.HTTP_SERVER_PORT, data=json.dumps(requestData))

print r.text
