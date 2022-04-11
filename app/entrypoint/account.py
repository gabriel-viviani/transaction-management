from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from repository.database import get_db
from service.account import get_acc
from dto.account import Account

router = APIRouter()


@router.get(
    "/{account_id}",
    status_code=status.HTTP_200_OK,
    response_model=Account,
)
def get_account(account_id: str, db: Session = Depends(get_db)) -> Account:
    return get_acc(db, account_id)
