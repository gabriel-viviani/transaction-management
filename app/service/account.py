from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from dto.account import Account
from repository.account import get_acc_by_id, save_account


def get_acc(db: Session, id: str) -> Account:
    acc = get_acc_by_id(db, id)

    if not acc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Account {id}, not found."
        )

    return Account(account_id=acc.account_id, balance=acc.balance)


def create_acc(db: Session, id: str) -> Account:
    new_acc = save_account(db, id)

    return Account(account_id=new_acc.account_id, balance=new_acc.balance)
