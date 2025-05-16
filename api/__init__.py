from fastapi import APIRouter
from .endpoints import user, role, auth, transport, delivery
# from . import events

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(role.router, prefix="/roles", tags=["roles"])
router.include_router(user.router, prefix="/users", tags=["users"])
router.include_router(delivery.router, prefix="/delivery", tags=["delivery"])
router.include_router(transport.router, prefix="/transport", tags=["transport"])