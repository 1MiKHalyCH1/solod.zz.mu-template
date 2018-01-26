from tornado_mysql import connect
from bcrypt import checkpw, hashpw, gensalt
from getpass import getpass
from config import db_config
from tornado import gen, ioloop

SQL = "INSERT INTO users(login, password) VALUES(%s, %s)"

@gen.coroutine
def add_admin(login, password):
    hash_pass = hashpw(password, gensalt())
    conn = yield connect(**db_config)
    cur = conn.cursor()
    yield cur.execute(SQL, (login, hash_pass))
    cur.close()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    login = input('Login: ')
    password = getpass('Password: ')
    ioloop.IOLoop.current().run_sync(lambda: add_admin(login, password))