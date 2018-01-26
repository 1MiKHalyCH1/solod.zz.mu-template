#!/usr/bin/env python3

import tornado_mysql

from tornado.options import options, define
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado import gen
from copy import deepcopy
from json import loads

from handlers import *
from config import *
from db import DbHandler


def generate_sitemap():
    with open("map.json", "r") as f:
        sitemap = loads(f.read())

    res = []
    for name, template in sitemap.items():
        res.append(("/{}".format(name), DefaultHandler, {"template":template}))
    return res

class MainApplication(Application):
    def __init__(self):
        db_handler = DbHandler(db_config)
        handlers = generate_sitemap() + [
            ("/news", NewsHandler, {"db":db_handler}),
            ("/admin", AdminHandler, {"db":db_handler}),
            ("/login", LoginHandler, {"db":db_handler})
        ]        
        Application.__init__(self, handlers, default_handler_class=Handler404, **aplication_config)
        print('[+] Server started at http://{}:{}'.format(options.host, options.port))

if __name__ == "__main__":
    define("host", default="localhost", help="app host", type=str)
    define("port", default=8888, help="app port", type=int)
    
    app = HTTPServer(MainApplication())
    app.listen(options.port)
    IOLoop.instance().start()