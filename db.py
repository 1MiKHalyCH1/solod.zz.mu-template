from tornado import gen
from tornado_mysql import connect
from dbconfig import db_config
from datetime import date


class News:
    def __init__(self, id, title, body, d):
        self.id = id
        self.title = title
        self.body = body
        self.date = d


class DbNewsHandler():
    def __init__(self):
        self.SELECT_ALL = "SELECT * FROM news ORDER BY id DESC"
        self.INSERT = "INSERT INTO news(title, body, d) VALUES (%s,%s,%s)"
        self.DELETE = "DELETE FROM news WHERE id=%s"

    @gen.coroutine
    def _start_cursor(self):
        self.conn = yield connect(**db_config)
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
        raise gen.Return(news)

    @gen.coroutine
    def add_news(self, title, body):
        d = date.today().strftime('%d-%m-%y')
        yield self._start_cursor()
        yield self.cur.execute(self.INSERT, (title,body,d))
        yield self.cur.execute(self.SELECT_ALL)
        news = [News(*e) for e in self.cur]
        yield self._close_cursor()
        raise gen.Return(news)

    @gen.coroutine
    def delete_news(self, id):
        yield self._start_cursor()
        yield self.cur.execute(self.DELETE, (int(id)))
        yield self.cur.execute(self.SELECT_ALL)
        news = [News(*e) for e in self.cur]
        yield self._close_cursor()
        raise gen.Return(news)