from os.path import dirname, join

db_config = dict(
    host='localhost',
    user='solod',
    passwd='solod',
    db='solod',
    charset='utf8'
)

aplication_config = dict(
    cookie_secret='w9R9Y7/wQIC9MF21PHc+DVH8mxkNykWNimojniV/j8o=',
    login_url="/login",
    xsrf_cookies=True,
    static_path=join(dirname(__file__), "static"),
    template_path=join(dirname(__file__), "templates")
)