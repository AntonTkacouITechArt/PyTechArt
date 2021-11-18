from sqlalchemy import Column, Integer, String, Text, CheckConstraint
from .base import Base


class Online(Base):
    """Table onliner. It keep all online users"""
    __tablename__ = 'online'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    id_chatroom = Column(Integer(), nullable=False)
    __table_args__ = (
        CheckConstraint('id_chatroom > 0 and id_chatroom < 12',
                        name='CK_checkroom'
                        ),
    )
