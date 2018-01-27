from config import db_config
from tornado_mysql import connect
from getpass import getpass
from tornado import gen, ioloop

@gen.coroutine
def db_adj(root, passwd):
    conn = yield connect(host=db_config['host'], charset=db_config['charset'], user=root, passwd=passwd)
    cur = conn.cursor()
    yield cur.execute('DROP USER IF EXISTS %s@%s', (db_config['user'], db_config['host']))
    yield cur.execute('CREATE USER %s@%s IDENTIFIED BY %s', (db_config['user'], db_config['host'], db_config['passwd']))
    yield cur.execute('GRANT ALL PRIVILEGES ON * . * TO %s@%s', (db_config['user'], db_config['host']))
    yield cur.execute('FLUSH PRIVILEGES')
    cur.close()
    conn.commit()
    conn.close()
    print('USER CREATED!')

    conn = yield connect(host=db_config['host'], charset=db_config['charset'], user=db_config['user'], passwd=db_config['passwd'])
    cur = conn.cursor()
    yield cur.execute('DROP DATABASE IF EXISTS {}'.format(db_config['db']))
    yield cur.execute('CREATE DATABASE {}'.format(db_config['db']))
    cur.close()
    conn.commit()
    conn.close()
    print('DATABASE CREATED!')

    conn = yield connect(**db_config)
    cur = conn.cursor()
    yield cur.execute('CREATE TABLE news (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, title VARCHAR(30), body VARCHAR(700), d CHAR(8))')
    yield cur.execute('CREATE TABLE users(login VARCHAR(20) PRIMARY KEY, password VARCHAR(65))')
    cur.close()
    conn.commit()
    conn.close()
    print('TABLES CREATED!')

    print('Done!')
    print('Now you need to create administrator using `python3 new_admin.py`')

if __name__ == "__main__":
    root = input('Your root login for mysql: ')
    passwd = getpass('Your root password: ')

    ioloop.IOLoop.current().run_sync(lambda: db_adj(root, passwd))