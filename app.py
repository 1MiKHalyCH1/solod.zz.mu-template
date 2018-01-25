#!/usr/bin/env python3

import os.path as ospath

from tornado.options import options, define
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from copy import deepcopy
from json import loads

from handlers import *



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
            "static_path": ospath.join(ospath.dirname(__file__), "static"),
            "template_path": ospath.join(ospath.dirname(__file__), "templates"),
            "default_handler_class": Handler404
        }
        Application.__init__(self, handlers, **settings)
        print('[+] Server started at http://{}:{}'.format(options.host, options.port))

if __name__ == "__main__":
    define("host", default="localhost", help="app host", type=str)
    define("port", default=8888, help="app port", type=int)
    
    app = HTTPServer(MainApplication())
    app.listen(options.port)
    IOLoop.instance().start()