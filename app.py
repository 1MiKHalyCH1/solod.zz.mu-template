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


class DirectoryHandler(RequestHandler):
    def initialize(self, template, children):
        self.template = template
        self.children = children

    def get(self, child):
        if child in self.children:
            self.render(os.path.join(self.template, self.children[child]))
        else:
            self.write("There are no page with this name in '{}'<br>Try this:<br>".format(self.template))
            self.write('<br>'.join('<a href="/{}/{}">{}</a>'.format(self.template, k,k) for k in self.children))


def generate_sitemap():
    with open("map.json", "r") as f:
        sitemap = loads(f.read())

    res = []
    for name, template in sitemap.items():
        if type(template) == str:
            res.append(("/{}".format(name), DefaultHandler, {"template":template}))
        elif type(template) == dict:
            res.append(("/{}/(.*)".format(name), DirectoryHandler, {"template":name, "children":template}))
    return res

class MainApplication(Application):
    def __init__(self):
        handlers = generate_sitemap()
        settings = {
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "debug" : True  #TODO: remove before production
        }
        Application.__init__(self, handlers, **settings)
        print('[+] Server started')

if __name__ == "__main__":
    app = HTTPServer(MainApplication())
    app.listen(8888)
    IOLoop.instance().start()