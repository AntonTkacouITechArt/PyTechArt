import logging
import tornado.websocket

# from DB_manager import manager
from models.Messages import Messages


class MessageWebSocket(tornado.websocket.WebSocketHandler):
    waiters = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
        '10': [],
    }

    @classmethod
    def send_updates(cls, chatroom: str, msg: str):
        for waiter in cls.waiters.get(chatroom):
            try:
                waiter.write_message(msg)
            except:
                logging.error("Error sending message", exc_info=True)
                raise

    def open(self, *args):
        self.request.chatroom = args[0][0]
        self.current_user = self.get_secure_cookie('user').decode("utf-8")
        if self.current_user in [x.current_user for x in
                                 MessageWebSocket.waiters[args[0][0]]]:
            self.write_message("ERROR >>> Sorry, but user with such name "
                               "connected!!")
            self.on_close(two_same_username=True)
        else:
            MessageWebSocket.waiters[args[0][0]].append(self)

    def on_message(self, message, *args):

        # >>>>>>
        # add code about add message in DB
        msg = Messages(
            username=self.get_secure_cookie("user"),
            text_message=message,
            id_chatroom=self.request.chatroom,
        )
        # with manager.session.begin() as session:
        #     session.session.add(msg)

        # <<<<<<<

        output = self.current_user + u": " + message
        MessageWebSocket.send_updates(self.request.chatroom, output)

    def on_close(self, two_same_username=False):
        if not two_same_username and self.current_user in [x.current_user for x in
                                 MessageWebSocket.waiters[self.request.chatroom]]:
            MessageWebSocket.waiters[self.request.chatroom].pop(self)

    def check_origin(self, origin):
        return True
