from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .. import Base

class Delivery(Base):
    __tablename__ = 'delivery'

    id = Column(Integer, primary_key=True)
    user_delivery_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # transport = Column(String(512), nullable=False, default='')
    weight = Column(Integer, nullable=False, default=0)
    kind = Column(String(255), nullable=False, default='')
    dimensions = Column(String(255), nullable=False, default='')
    status = Column(String(255), nullable=False, default='')
    address_in = Column(String(512), nullable=False, default='')
    address_out = Column(String(512), nullable=False, default='')
    datetime_in = Column(DateTime(timezone=True), nullable=True)
    datetime_out = Column(DateTime(timezone=True), nullable=True)

#    transport = relationship("MonitoredProduct", back_populates="products")

    def __repr__(self):
        return f"<Delivery(id='{self.id}', user_delivery_id='{self.user_delivery_id}', status='{self.status}')>"
