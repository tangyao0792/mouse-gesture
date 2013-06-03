import mouse
import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class MouseHandler(tornado.web.RequestHandler):
    def post(self):
        dataX_str = self.get_argument('dataX')[: -1]
        dataY_str = self.get_argument('dataY')[: -1]
        dataX = map(int, dataX_str.split(','))
        dataY = map(int, dataY_str.split(','))
        print len(dataX)
        n = mouse.verify(dataX, dataY)
        if n == 1:
            self.write('too small!')
        else:
            self.write('%d' % n )

handlers=[
    (r"/", IndexHandler),
    (r"/mouse", MouseHandler)
]

static_path=os.path.join(os.path.dirname(__file__), 'static')

if __name__ == "__main__":
    try:
        app = tornado.web.Application(
            handlers=handlers,
            static_path=static_path
        )
        tornado.options.parse_command_line()
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        print e
        pass
 
