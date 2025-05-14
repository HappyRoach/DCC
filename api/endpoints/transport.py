from typing import List

from fastapi import APIRouter, Depends, HTTPException

from .. import crud
from .. import security
from ..schemas import transport as schemas
from ..utils.database import get_db, Session
from database.schemas.user import User

router = APIRouter()


@router.post("/", response_model=schemas.TransportGet)
def create_transport(
    transport: schemas.TransportCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    return crud.create_transport(db=db, transport=transport)


@router.get("/", response_model=List[schemas.TransportGet])
def get_transports(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    return crud.get_transports(db)


@router.get("/{transport_id}", response_model=schemas.TransportGet)
def get_transport(
    transport_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin", "manager"]))
):
    db_transport = crud.get_transport(db, transport_id=transport_id)
    if db_transport is None:
        raise HTTPException(status_code=404, detail="Transport not found")
    return db_transport


@router.put("/{transport_id}", response_model=schemas.TransportGet)
def update_transport(
    transport_id: int,
    transport: schemas.TransportUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_transport = crud.update_transport(db=db, transport_id=transport_id, transport=transport)
    if db_transport is None:
        raise HTTPException(status_code=404, detail="Transport not found")
    return db_transport


@router.delete("/{transport_id}")
def delete_transport(
    transport_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.check_role(["superadmin", "admin"]))
):
    db_transport = crud.delete_transport(db, transport_id=transport_id)
    if db_transport is None:
        raise HTTPException(status_code=404, detail="Transport not found")
    return {"message": "Transport deleted successfully"}
