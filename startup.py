from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application


class TestHandler(RequestHandler):
    def get(self):
        self.write("first application")


def make_app():
    return Application([
        (r"/", TestHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
