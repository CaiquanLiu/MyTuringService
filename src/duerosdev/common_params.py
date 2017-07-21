# coding:utf8
'''
Created on 2017年7月21日

@author: liucaiquan
'''
bearer='Bearer '# 注意空格
# 临时使用度秘”AI小助手“的Token
token='23.027c7321a14bdbf673adc59b154b43b1.2592000.1502956721.2550887388-9874433'
authorization=bearer+token
# 临时使用小米5S测试机的DeviceID
dueros_device_id='ffffffff-e76f-1bdf-0000-000063ec21a0'

# 主机地址
host='dueros-h2.baidu.com'

# 长链接路径
path_get_directives='/dcs/v1/directives'

# 语音上传路径
path_upload_voice_data='/dcs/v1/events'

# Multipart 分隔符
boundary='this-is-a-boundary'

# 换行分隔符
crlf = '\r\n'
