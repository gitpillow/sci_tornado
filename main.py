import tornado.ioloop
import tornado.web

from handler.latex_python import LatexMatrix

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, World")
    
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/latex/matrix", LatexMatrix),
    ])

if __name__ == "__main__":
    print("main")
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()