from apps.__common__.models import TimeStampMixin
from db import db


class Transaction(TimeStampMixin):
    __tablename__ = "transactions"

    class TransactionType:
        CREDIT  = "credit"
        DEBIT   = "debit"

    id              = db.Column(db.BigInteger, primary_key=True)
    type            = db.Column(db.String(64))
    amount          = db.Column(db.Float, default=0)
    parent_id       = db.Column(db.BigInteger)

    def json(self):
        return {
            "type"      : self.type,
            "amount"    : self.amount,
            "parent_id" : self.parent_id
        }