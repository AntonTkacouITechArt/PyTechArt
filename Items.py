class Items(Base):
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text())
    price = Column(Numeric(50, 3))
    department_id = Column(ForeignKey('departments.id'))
    departments = relationship(
        'Departments', cascade='all, delete, delete-orphan'
    )
    __table_args__ = (
        CheckConstraint('price > -1', name='items_price_check'),
    )