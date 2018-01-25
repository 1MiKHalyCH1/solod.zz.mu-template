from tornado.web import RequestHandler

class DefaultHandler(RequestHandler):
    def initialize(self, template):
        self.template = template

    def get(self):
        self.render(self.template)