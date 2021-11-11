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


def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            url(r'/', MainHandler, name="index"),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
