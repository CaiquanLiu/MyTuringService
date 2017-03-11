# coding:utf-8
import tornado.ioloop
import tornado.web
import json
from turing.turing import Turing
import common_params

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
    
    def post(self):
#         print self.request.body
        rst = self.process(self.request.body)
        print 'process rst: '+rst
        self.write(rst)
        
    # post处理函数
    def process(self, params):
        if(params is None):
            print 'params is None!'
            return
        
        try:
            req_dic = json.loads(params)
        except ValueError:
            print ' params is not Json format!'
            return
        
        if(not req_dic.has_key(common_params.KEY_REQUEST_TYPE)):
            print 'request does not contain request type field!'
         
        req_type = req_dic[common_params.KEY_REQUEST_TYPE]
        
        # 请求类型为turing请求
        if(req_type == common_params.REQUEST_TYPE_TURING):
            if(not req_dic.has_key(common_params.REQUEST_TURING_CONTENT)):
                print common_params.REQUEST_TURING_CONTENT + " is None!"
                return
            
            print 'turing request params: ' + req_dic[common_params.REQUEST_TURING_CONTENT]
            turing_instance = Turing()
            return turing_instance.request(req_dic[common_params.REQUEST_TURING_CONTENT]).text
        # 请求类型为其他的请求







#     def __init__(self):
#         self.turing_instance = Turing()





# 以下为http service启动逻辑
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    

