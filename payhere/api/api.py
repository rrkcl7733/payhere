from fastapi import APIRouter, Depends

from payhere.api.api_v1.endpoints import login, account

api_router = APIRouter()
api_router.include_router(
    login.router,
    tags=["login"])
api_router.include_router(
    account.router,
    prefix="/accounts",
    tags=["account"],
    # dependencies=[Depends(get_current_user)]
)