import tornado
import tornado.websocket
from DB_manager import Session
from Websocket import MessageWebSocket, ChatRoomWebSocket
from models.Messages import Messages


class BaseHandler(tornado.web.RequestHandler):
    """Abstract handler => should be inherited"""

    def get_current_user(self):
        return self.get_secure_cookie("user")

    def write_error(self, error=None, *args, **kwargs):
        self.write(f"Error! {error}!")


class MainHandler(BaseHandler):
    """Index page"""

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        name = tornado.escape.xhtml_escape(self.current_user)
        self.render("index.html", name=name)


class LoginHandler(BaseHandler):
    """Login page"""

    def get(self, *args, **kwargs):
        self.render('login.html')

    def post(self, *args, **kwargs):
        self.set_secure_cookie("user", self.get_argument("name"),
                               expires_days=1)
        self.redirect(self.reverse_url('index'))


class ChatHandler(BaseHandler):
    """Chatroom page"""

    @tornado.web.authenticated
    def get(self, chatroom: str, *args, **kwargs):
        if self.current_user == b"Admin" and chatroom == '11':
            self.redirect(self.reverse_url('admin'))
        elif int(chatroom) not in range(1, 11):
            self.write_error(f"Chatroom not found")
        else:
            messages = None
            with Session() as session:
                messages = [msg.username + ': ' + msg.text_message for msg in
                            session.query(Messages).filter(
                                Messages.id_chatroom == chatroom)]

            self.render('chat.html', name=self.current_user,
                        messages=messages, online=ChatRoomWebSocket.waiters,
                        chatroom=chatroom)

    def post(self, *args, **kwargs):
        self.redirect(self.reverse_url('index'))


class AdminHandler(BaseHandler):
    """Admin page"""

    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('admin.html')

    def post(self, *args, **kwargs):
        if self.get_body_argument('Clear', "False") == "True":
            with Session() as session:
                with session.begin():
                    try:
                        session.query(Messages).filter(
                            Messages.id_chatroom == self.get_body_argument(
                                'chatroom')
                        ).delete()
                    except:
                        session.rollback()
                        raise
        elif self.get_body_argument('Reload', "False") == "True":
            for x in MessageWebSocket.waiters[self.get_body_argument('chatroom')]:
                x.close()
        self.redirect(self.reverse_url('admin'))
