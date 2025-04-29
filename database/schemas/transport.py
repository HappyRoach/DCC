from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .. import Base

class Transport(Base):
    __tablename__ = 'transport'

    id = Column(Integer, primary_key=True)
    capacity = Column(Integer, nullable=False)
    dimensions = Column(String(512), nullable=True)

    #products = relationship("Product", back_populates="monitored_product", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<transport(name='{self.name}', capacity='{self.capacity}', dimensions='{self.dimensions}')>"
