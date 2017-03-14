# coding:utf-8
'''
Created on 2017年3月14日

@author: liucaiquan
'''
import json
from http_request import HttpRequest
class MyTts(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # token获取相关变量(使用MyNavi信息)
        self.token_request = HttpRequest("https://openapi.baidu.com/oauth/2.0/token")
        self.key_grant_type = "grant_type"
        self.value_grant_type = "client_credentials" 
        self.key_client_id = "client_id"
        self.value_client_id = "XWNntfdAttoOsshbTLI9d7BxWX4wO8Ye"
        self.key_client_secret = "client_secret"
        self.value_client_secret = "OU4fqmeeUQaAyoSNchvgk817lWRGRGnT"
        
        # 语音合成相关变量
        self.voice_request = HttpRequest("http://tsn.baidu.com/text2audio")
        self.key_tex = "tex"
        self.key_lan = "lan"
        self.value_lan = "zh"
        # token的有效期为一个月（2017-3-14th）
        self.key_tok = "tok"
        self.value_tok = "24.6f389722b04a319b23a9405b0150aec7.2592000.1492073691.282335-8404201"
        self.key_ctp = "ctp"
        self.value_ctp = 1
        self.key_cuid = "cuid"
        self.value_cuid = "eddy_eddy_eddy_eddy_eddy"
        
    def get_token(self):
        data = {self.key_grant_type:self.value_grant_type, \
              self.key_client_id:self.value_client_id, \
              self.key_client_secret:self.value_client_secret}
        res = self.token_request.get(params=data).text
        res_dic = json.loads(res)
        if(res_dic.has_key("access_token")):
            return res_dic["access_token"]
        else:
            return None
        
    
    def voice_synth(self, content):
        data = {self.key_tex:content, \
              self.key_lan:self.value_lan, \
              self.key_tok:self.value_tok, \
              self.key_ctp:self.value_ctp, \
              self.key_cuid:self.value_cuid}
        
        voice_data = self.voice_request.get(params=data).content
    
        voice_file = open("./voice.mp3", "wb")
        voice_file.write(voice_data)
        voice_file.close()
        
        
        
        
