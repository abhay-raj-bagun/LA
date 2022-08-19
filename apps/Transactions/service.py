from .models import Transaction
from db import db


def create_transaction(transaction_id, payload):
    # Get all the required values
    amount = payload.get("amount")
    type   = payload.get("type")
    parent_id = payload.get("parent_id", None)

    # add a new Transaction
    new_transaction = Transaction(
        id = transaction_id,
        type = type,
        amount = amount,
        parent_id = parent_id
    )
    db.session.add(new_transaction)
    db.session.commit()


def get_transaction_by_id(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id,deleted_at=None).first()
    return transaction.json()


def get_transactions_by_type(type):
    id_list = []
    transactions = Transaction.query.filter_by(type=type,deleted_at=None).all()
    for transaction in transactions:
        id_list.append(transaction.id)
    return id_list


def get_transaction_sum(transaction_id):
    transaction = Transaction.query.filter_by(id=transaction_id,deleted_at=None).first()
    if not transaction:
        raise Exception(f"Transaction not found! Transaction id = {transaction_id}")
    final_amount = transaction.amount
    child_transactions = Transaction.query.filter_by(parent_id=transaction_id,deleted_at=None).all()
    if not child_transactions:
        return transaction.amount
    for child in child_transactions:
        final_amount += get_transaction_sum(child.id)
    return final_amount