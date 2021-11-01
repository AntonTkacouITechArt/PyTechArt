from base import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, \
    CheckConstraint
from sqlalchemy.orm import relationship


class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text())
    price = Column(Numeric(50, 3))
    department_id = Column(ForeignKey('departments.id'))
    departments = relationship(
        'Departments',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        back_populates='items'
    )
    __table_args__ = (
        CheckConstraint('price > -1', name='items_price_check'),
    )
