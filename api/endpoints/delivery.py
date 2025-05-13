from typing import List

from fastapi import APIRouter, Depends, HTTPException

from .. import crud
from .. import security
from ..schemas import delivery as schemas
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()


@router.post("/", response_model=schemas.DeliveryGet)
def create_delivery(
    delivery: schemas.DeliveryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_user_with_role)
):
    return crud.create_delivery(db=db, delivery=delivery, user_id=current_user.id)


@router.get("/", response_model=List[schemas.DeliveryGet])
def get_deliveries(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    return crud.get_deliveries(db)


@router.get("/user/me", response_model=List[schemas.DeliveryGet])
def get_my_deliveries(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_user_with_role)
):
    return crud.get_user_deliveries(db=db, user_id=current_user.id)


@router.get("/{delivery_id}", response_model=schemas.DeliveryGet)
def get_delivery(
    delivery_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    db_delivery = crud.get_delivery(db, delivery_id=delivery_id)
    if db_delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")
    if db_delivery.user_delivery_id != current_user.id and current_user.role.name not in ["superadmin", "admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized to access this delivery")
    return db_delivery


@router.put("/{delivery_id}", response_model=schemas.DeliveryGet)
def update_delivery(
    delivery_id: int,
    delivery: schemas.DeliveryUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    db_delivery = crud.get_delivery(db, delivery_id=delivery_id)
    if db_delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")
    if db_delivery.user_delivery_id != current_user.id and current_user.role.name not in ["superadmin", "admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized to update this delivery")
    return crud.update_delivery(db=db, delivery_id=delivery_id, delivery=delivery)


@router.delete("/{delivery_id}")
def delete_delivery(
    delivery_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    db_delivery = crud.get_delivery(db, delivery_id=delivery_id)
    if db_delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")
    if db_delivery.user_delivery_id != current_user.id and current_user.role.name not in ["superadmin", "admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this delivery")
    crud.delete_delivery(db=db, delivery_id=delivery_id)
    return {"message": "Delivery deleted successfully"}
