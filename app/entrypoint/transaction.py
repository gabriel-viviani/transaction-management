from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from service.transaction import get_transaction, get_transactions, add_transaction
from dto.transaction import Transaction, ArrayOfTransactions, TransactionRequest
from . import check_content_type
from repository.database import get_db

router = APIRouter()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ArrayOfTransactions,
)
def get_all(db: Session = Depends(get_db)) -> ArrayOfTransactions:
    return get_transactions(db)


@router.get(
    "/{transaction_id}",
    status_code=status.HTTP_200_OK,
    response_model=Transaction,
)
def get_by_id(transaction_id: str, db: Session = Depends(get_db)) -> Transaction:
    return get_transaction(db, transaction_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Transaction,
    dependencies=[Depends(check_content_type)],
)
def create(
    new_transaction: TransactionRequest, db: Session = Depends(get_db)
) -> Transaction:
    return add_transaction(db, new_transaction)
