class Shops(Base):
    __tablename__ = 'shops'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    address = Column(Text())
    staff_amount = Column(Integer())
    __table_args__ = (
        CheckConstraint('staff_amount > -1',
                        name='shops_staff_amount_check')
    )
    departments = relationship(
        'Departments', cascade='all, delete, delete-orphan'
    )