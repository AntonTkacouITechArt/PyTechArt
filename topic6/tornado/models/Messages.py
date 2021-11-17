from sqlalchemy import Column, Integer, String, Text, CheckConstraint
from .base import Base


class Messages(Base):
    """Table messages. It keep all messages"""
    __tablename__ = 'messages'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    text_message = Column(Text())
    id_chatroom = Column(Integer(), nullable=False)
    __table_args__ = (
        CheckConstraint('id_chatroom > 0 and id_chatroom < 12',
                        name='items_price_check'
                        ),
    )
