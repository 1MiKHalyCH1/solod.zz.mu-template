from tornado.web import RequestHandler, authenticated
from tornado import gen

class AdminHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    @gen.coroutine
    def get(self):
        if self.get_secure_cookie("admin"):
            news = yield self.db.get_all_news()
            self.render("news-admin.html", news=news)
        else:
            self.redirect("/login")
    
    @gen.coroutine
    def post(self):
        if self.get_secure_cookie("admin"):
            if 'title' in self.request.arguments:
                title = self.get_argument('title', strip=True) 
                body = self.get_argument('body', strip=True)
                yield self.db.add_news(title, body)
            elif 'id' in self.request.arguments:
                id = self.get_argument('id', strip=True)
                yield self.db.delete_news(id)
            self.redirect("/admin")
        else:
            self.redirect("/login")