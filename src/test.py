# coding:utf-8
# 图灵接口测试
# from turing.turing import Turing
# 
# turing = Turing()
# response = turing.request("今天天气怎么样呀？")
# print response.text

# finalseg分词测试
# from utils.word_seg_finalseg import Finalseg
# 
# seg=Finalseg()
# 
# sentence="请给我讲一个故事"
# 
# rst=seg.cut(sentence)
# 
# print "/ ".join(rst)

# TTS token测试
# import json
# from utils.tts import MyTts
# tts = MyTts()
# 
# # print tts.get_token()
# tts.voice_synth("妈蛋！你个二货！")

#Wechat token测试
from wechat.material_operation import MaterialOperation

material_operation=MaterialOperation()

# print material_operation.get_token()
print material_operation.upload("./voice.mp3")




    
