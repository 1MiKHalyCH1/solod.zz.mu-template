from tornado.web import RequestHandler
from datetime import date


class News:
    def __init__(self, title, body, d):
        self.title = title
        self.body = body
        self.date = d

class NewsHandler(RequestHandler):
    def get(self):
        first = News('Title', 'first', str(date.today()))
        second = News('Title', 'second', str(date.today()))
        news = [first, second]
        self.render("news.html", news=news)