from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

from .. import Base


class DeliveryStatus(str, enum.Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"


class Delivery(Base):
    __tablename__ = 'deliveries'

    id = Column(Integer, primary_key=True)
    user_delivery_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    weight = Column(Integer, nullable=False)  # Weight in kilograms
    status = Column(Enum(DeliveryStatus), nullable=False, default=DeliveryStatus.PENDING)
    dimensions = Column(String, nullable=False)
    address_in = Column(String, nullable=False)
    address_out = Column(String, nullable=False)
    datetime_in = Column(DateTime, nullable=False)
    datetime_out = Column(DateTime, nullable=False)
    transport_id = Column(Integer, ForeignKey('transports.id'), nullable=False)

    # Relationships
    user = relationship("User", back_populates="deliveries")
    transport = relationship("Transport", back_populates="deliveries")

    def __repr__(self):
        return f"<Delivery(id='{self.id}', status='{self.status}', user_id='{self.user_delivery_id}')>"
