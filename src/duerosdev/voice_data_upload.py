# coding:utf-8
'''
Created on 2017年7月21日
基于Http/2 MultiPart上传语音数据到DuerOS云端
@author: liucaiquan
'''
from common_params import host, authorization, dueros_device_id, path_upload_voice_data, boundary,crlf
from hyper import HTTP20Connection
import json
import wave
class VoiceDataUpload(object):
    '''
            参考：
            http://axiaoxin.com/article/216/
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.conn = HTTP20Connection(host)
        self.headers={'authorization':authorization, \
                 'dueros-device-id':dueros_device_id, \
                 'content-type':'multipart/form-data; boundary={0}'.format(boundary)}
        
    
    '''
        msg_id：消息ID（messageId字段）
        dialog_req_id：对话ID（dialogRequestId字段）
        format：语音数据格式（format字段）
        data：语音raw data（pcm数据流）
    '''
    def get_multipart_formed_data(self, msg_id, dialog_req_id, format, data):
        
        event={'clientContext':['ai.dueros.device_interface.alerts.AlertsState','ai.dueros.device_interface.audio_player.PlaybackState','ai.dueros.device_interface.speaker_controller.VolumeState','ai.dueros.device_interface.voice_output.SpeechState'], \
       'event':{'header':{'namespace':'ai.dueros.device_interface.voice_input', \
                          'name':'ListenStarted', \
                          'messageId':msg_id, \
                          'dialogRequestId':dialog_req_id}, \
                'payload':{'format':format}}}
        
        event=json.dumps(event)
        
        post_data1=[]
        
        # ListenStarted事件
        post_data1.append('--'+boundary)
        post_data1.append('Content-Disposition: form-data; name="metadata"')
        post_data1.append('Content-Type: text/plain; charset=utf-8')
        post_data1.append('')
        post_data1.append(event)
    #     post_data1.append('--'+boundary+'--')# test
        post_data1.append('')
        
    #     return crlf.join(post_data1).encode('utf-8')# test
        
    #     # Audio data
        post_data1.append('--'+boundary)
        post_data1.append('Content-Disposition: form-data; name="audio"')
        post_data1.append('Content-Type: application/octet-stream')
        post_data1.append('')
         
        body1=crlf.join(post_data1).encode('utf-8')
         
        body2=data
         
        post_data3=[]
        post_data3.append('--'+boundary+'--')
        post_data3.append('')
        body3=crlf.join(post_data3).encode('utf-8')
         
        upload_data=body1+b'{0}'.format(crlf)+body2+b'{0}'.format(crlf)+body3
         
        return upload_data
    
    '''
        msg_id：消息ID（messageId字段）
        dialog_req_id：对话ID（dialogRequestId字段）
        format：语音数据格式（format字段）
        data：语音raw data（pcm数据流）
    '''
    def voice_raw_data_upload(self, msg_id, dialog_req_id, format, data):
        post_body=self.get_multipart_formed_data(msg_id, dialog_req_id, format, data)
        self.conn.request('POST', path_upload_voice_data, headers=self.headers, body=post_body)
        resp = self.conn.get_response()
          
        return resp.read()
        