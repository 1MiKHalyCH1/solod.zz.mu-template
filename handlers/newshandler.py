from tornado.web import RequestHandler
from tornado import gen

class NewsHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    @gen.coroutine
    def get(self):
        news = yield self.db.get_all_news()
        self.render("news.html", news=news)