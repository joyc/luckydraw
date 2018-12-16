from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
import uuid
import datetime


class Histories(Base):
    __tablename__ = 'histories'
    id = Column(String(50), primary_key=True)
    create_time = Column(DateTime(), nullable=True)
    restaurant_id = Column(String(50), ForeignKey('restaurants.id'))

    def __init__(self, restaurant_id):
        self.id = str(uuid.uuid4())
        self.create_time = datetime.datetime.now()
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return '<History %r>' % (self.name)
