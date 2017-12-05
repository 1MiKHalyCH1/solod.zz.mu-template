import os

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer


class MainHandler(RequestHandler):
    def get(self):
        self.render("./static/index.html")

class BiographyHandler(RequestHandler):
    def get(self):
        self.render("./static/biography.html")

class CourseHandler(RequestHandler):
    def get(self, course_name):
        if course_name == "scripts":
            self.render("./static/edu/scripts.html")
        else:
            self.write(course_name)

class MainApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/biography", BiographyHandler),
            (r"/edu/(.*)", CourseHandler)
        ]
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static")
        }
        Application.__init__(self, handlers, **settings)

if __name__ == "__main__":
    app = HTTPServer(MainApplication())
    app.listen(8888)
    IOLoop.instance().start()