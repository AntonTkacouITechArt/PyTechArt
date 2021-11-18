import logging
import tornado.websocket
from sqlalchemy import and_
from DB_manager import Session
from models.Messages import Messages
from models.Online import Online


class BaseWebSocket(tornado.websocket.WebSocketHandler):
    @classmethod
    def send_updates(cls, chatroom: str, msg: str) -> None:
        for waiter in cls.waiters.get(chatroom):
            try:
                waiter.write_message(msg)
            except:
                logging.error("Error sending message", exc_info=True)
                raise

    def check_origin(self, origin):
        return True


class MessageWebSocket(BaseWebSocket):
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

    def open(self, *args, **kwargs):
        self.request.chatroom = args[0][0]
        self.current_user = self.get_secure_cookie('user').decode("utf-8")
        if self.current_user in [x.current_user for x in
                                 MessageWebSocket.waiters[
                                     self.request.chatroom]]:
            self.write_message("ERROR >>> Sorry, but user with such name "
                               "connected!!")
            self.close()
        else:
            MessageWebSocket.waiters[self.request.chatroom].append(self)

    def on_message(self, message, *args, **kwargs):
        MessageWebSocket.add_message(self.current_user, message,
                                     self.request.chatroom)
        output = self.current_user + u": " + message
        MessageWebSocket.send_updates(self.request.chatroom, output)

    def on_close(self, *args, **kwargs):
        if self.current_user in [x.current_user for x in
                                 MessageWebSocket.waiters[
                                     self.request.chatroom]]:
            self.add_message(self.current_user, u": disconnect from chatroom ",
                             self.request.chatroom)
            MessageWebSocket.waiters[self.request.chatroom].remove(self)
            MessageWebSocket.send_updates(self.request.chatroom,
                                          self.current_user + u": disconnect from chatroom ")

    @staticmethod
    def add_message(username: str, message: str, chatroom: str) -> None:
        msg = Messages(
            username=username,
            text_message=message,
            id_chatroom=chatroom,
        )
        with Session() as session:
            with session.begin():
                try:
                    session.add(msg)
                except:
                    session.rollback()
                    raise


class ChatRoomWebSocket(BaseWebSocket):
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

    def open(self, *args, **kwargs):
        self.request.chatroom = args[0][0]
        self.current_user = self.get_secure_cookie('user').decode("utf-8")
        ChatRoomWebSocket.waiters[self.request.chatroom].append(self)
        ChatRoomWebSocket.add_online(self.current_user, self.request.chatroom)
        ChatRoomWebSocket.send_updates(self.request.chatroom,
                                       self.current_user)

    def on_message(self, message, *args, **kwargs):
        # ChatRoomWebSocket.add_online(self.current_user, self.request.chatroom)
        # ChatRoomWebSocket.send_updates(self.request.chatroom, self.current_user)
        pass

    def on_close(self):
        ChatRoomWebSocket.delete_online(self.current_user,
                                        self.request.chatroom)
        ChatRoomWebSocket.waiters[self.request.chatroom].remove(self)

    @staticmethod
    def add_online(username: str, chatroom: str) -> None:
        msg = Online(
            username=username,
            id_chatroom=chatroom,
        )
        with Session() as session:
            with session.begin():
                try:
                    session.add(msg)
                except:
                    session.rollback()
                    raise

    @staticmethod
    def delete_online(username: str, chatroom: str) -> None:
        with Session() as session:
            with session.begin():
                try:
                    session.query(Online).filter(
                        and_(Online.username == username,
                             Online.id_chatroom == chatroom)
                    ).delete()
                except:
                    session.rollback()
                    raise
