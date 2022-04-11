from fastapi import APIRouter

from entrypoint import account, transaction

api_router = APIRouter()
api_router.include_router(account.router, prefix="/accounts", tags=["accounts"])
api_router.include_router(
    transaction.router, prefix="/transactions", tags=["transactions"]
)
