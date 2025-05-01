from typing import List, Optional

from sqlalchemy.orm import Session

from ..schemas import transport as schemas
from database.schemas import transport as models


def get_transport(db: Session, transport_id: int) -> Optional[models.Transport]:
    return db.query(models.Transport).filter(models.Transport.id == transport_id).first()


def get_transports(db: Session, skip: int = 0, limit: int = 100) -> List[models.Transport]:
    return db.query(models.Transport).offset(skip).limit(limit).all()


def create_transport(db: Session, transport: schemas.TransportCreate) -> models.Transport:
    db_transport = models.Transport(**transport.dict())
    db.add(db_transport)
    db.commit()
    db.refresh(db_transport)
    return db_transport


def update_transport(db: Session, transport_id: int, transport: schemas.TransportUpdate) -> Optional[models.Transport]:
    db_transport = get_transport(db, transport_id)
    if db_transport:
        update_data = transport.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_transport, key, value)
        db.commit()
        db.refresh(db_transport)
    return db_transport


def delete_transport(db: Session, transport_id: int) -> Optional[models.Transport]:
    db_transport = get_transport(db, transport_id)
    if db_transport:
        db.delete(db_transport)
        db.commit()
    return db_transport 