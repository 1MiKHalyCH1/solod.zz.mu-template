from tornado.web import RequestHandler

class Handler404(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('404.html')