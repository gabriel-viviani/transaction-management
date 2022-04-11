from sqlalchemy.orm import Session
from decimal import Decimal
from typing import Any

from model.account import Account


def get_acc_by_id(db: Session, id: str) -> Any:
    return db.query(Account).filter_by(account_id=id).first()


def save_account(db: Session, id: str) -> Account:
    acc = Account(account_id=id)

    db.add(acc)
    db.commit()

    db.refresh(acc)
    return acc


def update_balance(db: Session, id: str, amount: Decimal) -> None:
    acc = db.query(Account).filter_by(account_id=id).with_for_update().first()

    acc.balance += amount
    db.add(acc)
