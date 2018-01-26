from tornado.web import RequestHandler
from tornado import gen

class LoginHandler(RequestHandler):
    def initialize(self, db):
        self.db = db
    
    def get(self):
        self.render('login.html', user=self.get_secure_cookie("admin"))

    @gen.coroutine
    def post(self):
        login = self.get_argument("login", strip=True)
        password = self.get_argument("password", strip=True)
        res = yield self.db.check_admin(login, password)
        if res:
            self.set_secure_cookie("admin", login)
            self.redirect(self.get_argument("next", "/"))
        else:
            self.redirect("/login")
