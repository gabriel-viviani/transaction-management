from pydantic import BaseModel
from decimal import Decimal
from uuid import UUID


class Account(BaseModel):
    account_id: UUID
    balance: Decimal
