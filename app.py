#!/usr/bin/env python3

from json import loads
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from copy import deepcopy

import os

class DefaultHandler(RequestHandler):
    def initialize(self, template):
        self.template = template

    def get(self):
        self.render(self.template)

class Handler404(RequestHandler):
    def prepare(self):
        self.set_status(404)
        self.render('index.html')

def generate_sitemap():
    with open("map.json", "r") as f:
        sitemap = loads(f.read())

    res = []
    for name, template in sitemap.items():
        res.append(("/{}".format(name), DefaultHandler, {"template":template}))
    return res

class MainApplication(Application):
    def __init__(self):
        handlers = generate_sitemap()
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "default_handler_class": Handler404
        }
        Application.__init__(self, handlers, **settings)
        print('[+] Server started')

if __name__ == "__main__":
    app = HTTPServer(MainApplication())
    app.listen(8888)
    IOLoop.instance().start()