# coding:utf-8
'''
Created on 2017年7月15日

@author: Administrator
'''
from utils.http_request import HttpRequest
import json
class BaiduUnit(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # token获取(使用应用名称为：“才权的AI小助手”)
        self.token_request=HttpRequest("https://aip.baidubce.com/oauth/2.0/token")
        self.key_grant_type="grant_type"
        self.val_grant_type="client_credentials";
        self.key_client_id="client_id"
        self.val_client_id="CuT1rAmusoriIXG4zn1BHvvr"
        self.key_client_secret="client_secret"
        self.val_client_secret="LDoBVgtESUomBR5KvPVikESPXxWEbar7"
        
        # token(15th-July-2017)
        self.val_token="24.00986074615d4d643f9c31fedac9354e.2592000.1502643141.282335-9892240"
        
        self.unit_requet=HttpRequest("https://aip.baidubce.com/rpc/2.0/solution/v1/unit_utterance?access_token=24.00986074615d4d643f9c31fedac9354e.2592000.1502643141.282335-9892240")
    # 获取token
    def get_token(self):
        data = {self.key_grant_type:self.val_grant_type, \
              self.key_client_id:self.val_client_id, \
              self.key_client_secret:self.val_client_secret}
        res = self.token_request.get(params=data).text
        res_dic = json.loads(res)
        if(res_dic.has_key("access_token")):
            return res_dic["access_token"]
        else:
            return None
        
    
    '''
            用户query请求
            scene_id：场景ID
            query：用户query
            session_id：session ID
    '''
    def query_request(self, scene_id, query, session_id):
        data={"scene_id":scene_id, \
              "query":query, \
              "session_id":session_id}
        
        return self.unit_requet.post(json.dumps(data))
        
        
        
        
        
        
