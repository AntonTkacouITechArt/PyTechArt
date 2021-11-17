import os
import tornado.web
import tornado.ioloop
from tornado import options
from tornado.options import options, define, parse_command_line
from DB_manager import connect_db
from Handler import MainHandler, LoginHandler, ChatHandler, AdminHandler
from Websocket import MessageWebSocket
from sqlalchemy.exc import SQLAlchemyError

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode", type=bool)
define("db_user", default="postgres", help="user of DB", type=str)
define("db_password", default="1111", help="password of DB user")
define("db_host", default="127.0.0.2", help="DB host", type=str)
define("db_name", default="test2", help="DB name", type=str)

SETTINGS = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'debug': options.debug,
    "login_url": "/login",
    'cookie_secret': "__TODO:_GENERATE_A_RANDOM_VALUE_HERE__",
    "xsrf_cookies": True,
}

URL = [
    tornado.web.url(r'/', MainHandler, name="index"),
    # url(r'/index', tornado.web.RedirectHandler, dict(url=r"/")),
    tornado.web.url(r'/login', LoginHandler, name="login"),
    tornado.web.url(r'/([0-9]+)/', ChatHandler, name='chat'),
    tornado.web.url(r'/11/', AdminHandler, name='admin'),
    tornado.web.url(r'/([0-9]+)/websocket/', MessageWebSocket, name='message_websocket'),

]


def main():
    parse_command_line()
    try:
        connect_db(options.db_user, options.db_password,
                             options.db_host,
                             options.db_name)
    except (SQLAlchemyError, Exception) as error:
        print(f"Error with DB {error}")
        raise
    app = tornado.web.Application(
        URL,
        **SETTINGS,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
