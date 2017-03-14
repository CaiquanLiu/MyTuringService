# coding:utf-8
'''
Created on 2017年3月14日

@author: liucaiquan
'''
import requests
import json
from utils.http_request import HttpRequest
class MaterialOperation(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # 获取token参数
        self.token_http_request = HttpRequest("https://api.weixin.qq.com/cgi-bin/token")
        
        self.key_grant_type = "grant_type"
        self.val_grant_type = "client_credential"
        
        self.key_appid = "appid"
        self.val_appid = "wx92c1c0282f51459d"
        
        self.key_secret = "secret"
        self.val_secret = "426c769b13c884803e5d7a3b2eca146a"
        
        # 上传素材参数
        self.upload_url = "https://api.weixin.qq.com/cgi-bin/media/upload"
        
        # token的有效期为2小时
        self.key_access_token = "access_token"
        self.val_access_token = "daijaUJO-XmBrkXXXkdKCx1UWWZE7Fvw22ExFv23EUBcuitIfTVK82uiJNpLH_JyOS0NE0IW8POC2q5KDzf9NePl4Bw5kug2nrZ9aAsQb_73wPnL7Sveawlqrk5IbOv2ZLPeADAUGK"
        
        self.key_type = "type"
        self.val_type = "voice"
        
        self.key_media = "media"
    def get_token(self):
        data = {self.key_grant_type:self.val_grant_type, \
              self.key_appid:self.val_appid, \
              self.key_secret:self.val_secret}
        
        response_data = self.token_http_request.get(params=data).text
        
        res_dic = json.loads(response_data)
        
        if(res_dic.has_key("access_token")):
            return res_dic["access_token"]
        else:
            return None
    
    '''
    upload方法测试不通过
            参考：http://blog.csdn.net/wangtaoking1/article/details/50741208
    '''     
    def upload(self, content):
        data = {self.key_access_token: self.val_access_token, \
                self.key_type: self.val_type}
        
        files = {self.key_media:open(content, 'rb')}
        
        response = requests.post(self.upload_url, data=data, files=files)
        
        return response.text
        
