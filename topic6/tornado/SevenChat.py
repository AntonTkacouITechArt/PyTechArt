import os
import tornado.web
import tornado.ioloop
from tornado import options
from tornado.web import url
from tornado.options import options, define, parse_command_line

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index1.html")

    def on_finish(self) -> None:
        # print(self._status_code)
        print(self.get_status())
        print(self.get_body_arguments(name="h1"))
        print(self.get_query_arguments(name="h1"))
        print(self.get_current_user())
        print(self.get_template_namespace())
        print(self.get_template_path())
        print(self.static_url(""))
        # print(self.get)


class SecondMain(tornado.web.RequestHandler):
    def get(self):
        self.write(f'<a href="{self.reverse_url("index")}"> LINK <\a>')


SETTINGS = {
    'template_path': os.path.join(os.path.dirname(__file__), "templates"),
    'static_path': os.path.join(os.path.dirname(__file__), "static"),
    'debug': options.debug,
}

URL = [
    url(r'/', MainHandler, name="index"),
    url(r'/1/', SecondMain, name="seconde"),
    url(r'/index', tornado.web.RedirectHandler, dict(url=r"/")),
]


def main():
    parse_command_line()
    app = tornado.web.Application(
        URL,
        **SETTINGS,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
