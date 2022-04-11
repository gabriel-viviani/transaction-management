from repository.database import Base, generate_uuid, gen_now

from sqlalchemy.types import CHAR, NUMERIC, DATETIME
from sqlalchemy import Column, ForeignKey
from decimal import Decimal


class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(CHAR(32), primary_key=True, default=generate_uuid)
    account_id = Column(CHAR(32), ForeignKey("account.account_id"))
    amount = Column(NUMERIC(precision=3))
    created_at = Column(DATETIME, default=gen_now())

    def __init__(self, account_id: str, amount: Decimal):
        self.account_id = account_id
        self.amount = amount
