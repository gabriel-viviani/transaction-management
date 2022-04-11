from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from repository.transaction import (
    find_transaction,
    find_transactions,
    insert_transaction,
)
from service.account import create_acc, get_acc_by_id
from dto.transaction import Transaction, TransactionRequest
from model.transaction import Transaction as ModelTransaction
from repository.account import update_balance


def get_transaction(db: Session, id: str) -> Transaction:
    transaction = find_transaction(db, id)

    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Transaction {id} not found."
        )

    return Transaction(
        transaction_id=transaction.transaction_id,
        account_id=transaction.account_id,
        amount=transaction.amount,
        created_at=transaction.created_at,
    )


def get_transactions(db: Session) -> List[Transaction]:
    transactions = find_transactions(db)

    return [
        Transaction(
            transaction_id=transaction.transaction_id,
            account_id=transaction.account_id,
            amount=transaction.amount,
            created_at=transaction.created_at,
        )
        for transaction in transactions
    ]


def add_transaction(db: Session, transaction_req: TransactionRequest) -> Transaction:
    acc = get_acc_by_id(db, str(transaction_req.account_id))
    if not acc:
        acc = create_acc(db, str(transaction_req.account_id))

    transaction = ModelTransaction(
        account_id=str(acc.account_id), amount=transaction_req.amount
    )

    try:
        created_transaction = insert_transaction(db, transaction)
        update_balance(db, str(acc.account_id), created_transaction.amount)

        db.commit()
        db.refresh(created_transaction)

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(ex)
        )

    return Transaction(
        transaction_id=created_transaction.transaction_id,
        account_id=created_transaction.account_id,
        amount=created_transaction.amount,
        created_at=created_transaction.created_at,
    )
