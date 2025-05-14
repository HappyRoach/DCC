from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.orm import relationship

from .. import Base


class Transport(Base):
    __tablename__ = 'transports'

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)  # Capacity in kilograms
    dimensions = Column(String, nullable=False)  # Capacity by dimensions

    deliveries = relationship("Delivery", back_populates="transport")

    def __repr__(self):
        return f"<Transport(id='{self.id}', capacity='{self.capacity}', dimensions='{self.dimensions}')>" 