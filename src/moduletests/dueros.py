# coding:utf-8
'''
Created on 2017年7月19日

@author: liucaiquan
'''
import wave

# 读取音频数据
def read_wave_data(file_path):  
     #open a wave file, and return a Wave_read object  
    f = wave.open(file_path,"rb")  
    #read the wave's format infomation,and return a tuple  
    params = f.getparams()  
    #get the info  
    nchannels, sampwidth, framerate, nframes = params[:4]  
    #Reads and returns nframes of audio, as a string of bytes.   
    str_data = f.readframes(nframes)  
    #close the stream  
    f.close()   
    return str_data

if __name__ == '__main__':
#     # 接收directive的长链接测试
#     from duerosdev.directives_connection import DriectivesLongConnection
#     directives_conn=DriectivesLongConnection()
#     print directives_conn.get()
 
 ###################################################################   
    # 语音数据上传测试
    from duerosdev.voice_data_upload import VoiceDataUpload
    voice_data_upload=VoiceDataUpload()
    msg_id='123'
    dialog_req_id='456'
    format='AUDIO_L16_RATE_16000_CHANNELS_1'
    data=read_wave_data('./../../res/music1.wav')
    print voice_data_upload.voice_raw_data_upload(msg_id, dialog_req_id, format, data)
    
    
    
    