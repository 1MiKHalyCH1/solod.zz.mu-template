from tornado.web import RequestHandler
from tornado import gen

class LoginHandler(RequestHandler):
    def initialize(self, db):
        self.db = db
    
    def get(self):
        self.clear_cookie("admin")
        self.render('login.html', user=self.get_secure_cookie("admin"))

    @gen.coroutine
    def post(self):
        login = self.get_argument("login", strip=True)
        password = self.get_argument("password", strip=True)
        res = yield self.db.check_admin(login, password)
        if res:
            self.set_secure_cookie("admin", login)
            self.redirect("/admin")
        else:
            self.redirect("/login")
