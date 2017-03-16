#coding:utf-8
import tornado.ioloop
import tornado.web
from utils.word_seg_finalseg import Finalseg

class MainHandler(tornado.web.RequestHandler):
    def get(self):
#         self.write("Hello, world")
        self.render('./html/index.html')
    
    def post(self):
        content = self.get_argument('content')
        word_seg=Finalseg()
        rst = word_seg.cut(content)
        self.render('./html/response.html', seg_rst=rst)
    
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
