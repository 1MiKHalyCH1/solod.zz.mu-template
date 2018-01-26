from tornado.web import RequestHandler
from tornado import gen

class AdminHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    @gen.coroutine
    def get(self):
        news = yield self.db.get_all_news()
        self.render("news-admin.html", news=news)
    
    @gen.coroutine
    def post(self):
        if 'title' in self.request.arguments:
            title = self.get_argument('title', strip=True) 
            body = self.get_argument('body', strip=True)
            news = yield self.db.add_news(title, body)
            print(title, body)
        elif 'id' in self.request.arguments:
            id = self.get_argument('id', strip=True)
            news = yield self.db.delete_news(id)
            print(id)

        self.render("news-admin.html", news=news)
        