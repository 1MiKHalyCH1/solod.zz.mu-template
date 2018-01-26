from tornado import gen
from tornado_mysql import connect
from datetime import date
from bcrypt import checkpw


class News:
    def __init__(self, id, title, body, d):
        self.id = id
        self.title = title
        self.body = body
        self.date = d


class DbHandler():
    def __init__(self, config):
        self.config = config
        self.SELECT_ALL = "SELECT * FROM news ORDER BY id DESC"
        self.INSERT = "INSERT INTO news(title, body, d) VALUES (%s,%s,%s)"
        self.DELETE = "DELETE FROM news WHERE id=%s"
        self.LOGIN = "SELECT * FROM users WHERE login LIKE %s LIMIT 1"

    @gen.coroutine
    def _start_cursor(self):
        self.conn = yield connect(**self.config)
        self.cur = self.conn.cursor()
    
    @gen.coroutine
    def _close_cursor(self):
        self.cur.close()
        self.conn.commit()     
        self.conn.close_async()

    @gen.coroutine
    def get_all_news(self):
        yield self._start_cursor()
        yield self.cur.execute(self.SELECT_ALL)
        news = [News(*e) for e in self.cur]
        yield self._close_cursor()
        return news

    @gen.coroutine
    def add_news(self, title, body):
        d = date.today().strftime('%d-%m-%y')
        yield self._start_cursor()
        yield self.cur.execute(self.INSERT, (title,body,d))
        yield self._close_cursor()
        return

    @gen.coroutine
    def delete_news(self, id):
        yield self._start_cursor()
        yield self.cur.execute(self.DELETE, (int(id)))
        yield self._close_cursor()
        return

    @gen.coroutine
    def check_admin(self, login, password):
        yield self._start_cursor()
        yield self.cur.execute(self.LOGIN, (login))
        founded = self.cur.fetchone()
        yield self._close_cursor()      
        if not founded: 
            return False
        return login == founded[0] and checkpw(password, founded[1])