import tornado
import tornado.websocket
from models.Messages import Messages


class BaseHandler(tornado.web.RequestHandler):
    """Abstract handler => should be inherited"""
    def get_current_user(self):
        return self.get_secure_cookie("user")

    def write_error(self, status_code, error=None, **kwargs):
        self.write(f"Error! {error} You caused a {status_code} error.")


class MainHandler(BaseHandler):
    """Index page"""
    @tornado.web.authenticated
    def get(self):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render("index.html", name=name)


class LoginHandler(BaseHandler):
    """Login page"""
    def get(self):
        self.render('login.html')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"),
                               expires_days=1)
        self.redirect(self.reverse_url('index'))


class ChatHandler(BaseHandler):
    """Chatroom page"""
    @tornado.web.authenticated
    def get(self, chatroom: str):
        if self.current_user == b"Admin" and chatroom == '11':
            self.render('admin.html')
        elif int(chatroom) not in range(1, 11):
            self.write_error(f"{self.current_user} chatroom not found")
        else:
            # messages =  [(msg.username, msg.text_message) for msg in manager.session.query(Messages).filter(Messages.id_chatroom == chatroom)]
            self.add_header('user_name', self.current_user)
            self.render('chat.html', name=self.current_user, messages=["Kak dela"])

    def post(self):
        self.redirect(self.reverse_url('index'))

class AdminHandler(BaseHandler):
    """Admin page"""
    @tornado.web.authenticated
    def get(self):
        self.render('admin.html')

    def post(self):
        # print(*args)
        # print(**kwargs)
        print(self.request.__dict__)
        print(self.__dict__)
        # print(self.get_argument('chatroom'))
