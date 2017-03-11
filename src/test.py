# coding:utf-8
from turing.turing import Turing

turing = Turing()
response = turing.request("今天天气怎么样呀？")
print response.text

    
