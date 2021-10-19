from base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    sphere = Column(String(100), nullable=False)
    staff_amount = Column(Integer())
    shop_id = Column(ForeignKey('shops.id'))
    shops = relationship(
        'Shops', cascade='all, delete, delete-orphan'
    )
    items = relationship(
        'Items', cascade='all, delete, delete-orphan'
    )
    __table_args__ = (
        CheckConstraint('staff_amount > -1',
                        name='departments_staff_amount_check'),
    )
