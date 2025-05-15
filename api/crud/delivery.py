from typing import List, Optional

from sqlalchemy.orm import Session

from ..schemas import delivery as schemas
from database.schemas import delivery as models

__all__ = ["get_delivery", "get_deliveries", "get_user_deliveries", "create_delivery", "update_delivery", "delete_delivery"]

def get_delivery(db: Session, delivery_id: int) -> Optional[models.Delivery]:
    return db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()


def get_deliveries(db: Session, skip: int = 0, limit: int = 100) -> List[models.Delivery]:
    return db.query(models.Delivery).offset(skip).limit(limit).all()


def get_user_deliveries(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[models.Delivery]:
    return db.query(models.Delivery).filter(models.Delivery.user_delivery_id == user_id).offset(skip).limit(limit).all()


def create_delivery(db: Session, delivery: schemas.DeliveryCreate, user_id: int) -> models.Delivery:
    db_delivery = models.Delivery(**delivery.dict(), user_delivery_id=user_id)
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    return db_delivery


def update_delivery(db: Session, delivery_id: int, delivery: schemas.DeliveryUpdate) -> Optional[models.Delivery]:
    db_delivery = get_delivery(db, delivery_id)
    if db_delivery:
        update_data = delivery.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_delivery, key, value)
        db.commit()
        db.refresh(db_delivery)
    return db_delivery


def delete_delivery(db: Session, delivery_id: int) -> Optional[models.Delivery]:
    db_delivery = get_delivery(db, delivery_id)
    if db_delivery:
        db.delete(db_delivery)
        db.commit()
    return db_delivery 