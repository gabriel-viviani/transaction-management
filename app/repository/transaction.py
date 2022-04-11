from sqlalchemy.orm import Session
from typing import Any

from model.transaction import Transaction


def insert_transaction(db: Session, new_transaction: Transaction) -> None:
    db.add(new_transaction)

    return new_transaction


def find_transaction(db: Session, id: str) -> Transaction:
    return db.query(Transaction).filter_by(transaction_id=id).first()


def find_transactions(db: Session) -> Any:
    return db.query(Transaction).all()
