from repository.database import Base

from sqlalchemy.types import CHAR, NUMERIC
from sqlalchemy import Column


class Account(Base):
    __tablename__ = "account"

    account_id = Column(CHAR(32), primary_key=True)
    balance = Column(NUMERIC(precision=3))

    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0
