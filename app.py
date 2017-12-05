#!/usr/bin/env python3

import os

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer


class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")

class BiographyHandler(RequestHandler):
    def get(self):
        self.render("biography.html")

class ContactsHandler(RequestHandler):
    def get(self):
        self.render("contacts.html")

class PublicationsHandler(RequestHandler):
    def get(self):
        self.render("publications.html")

class CourseHandler(RequestHandler):
    def get(self, course_name):
        courses = ["os", "php", "scripts", "web", "pnm", "ip"] # TODO: load from config
        
        if course_name in courses:
            self.render("edu/{}.html".format(course_name))
        else:
            self.write("There are no course with name '{}'. \n".format(course_name))
            self.write("Try this:")
            for e in courses:
                self.write('<br><a href="{}">{}</a>'.format(*[e]*2))


class MainApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/biography", BiographyHandler),
            (r"/edu/(.*)", CourseHandler),
            (r"/publications", PublicationsHandler),
            (r"/contacts", ContactsHandler)
        ]
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