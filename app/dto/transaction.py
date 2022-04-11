from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import List
from uuid import UUID


class Transaction(BaseModel):
    transaction_id: UUID
    account_id: UUID
    amount: Decimal
    created_at: datetime


class TransactionRequest(BaseModel):
    account_id: UUID
    amount: Decimal


class ArrayOfTransactions(BaseModel):
    __root__: List[Transaction]
