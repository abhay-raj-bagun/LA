from flask import Blueprint, request, make_response
from .service import create_transaction as _create_transaction, get_transaction_by_id, get_transactions_by_type as _get_transaction_by_type, get_transaction_sum

transactions = Blueprint('Transactions', __name__)


@transactions.route("/transaction/<transaction_id>", methods=["PUT"])
def create_transaction(transaction_id):
    try:
        payload = request.get_json()
        _create_transaction(transaction_id, payload)
        return make_response({
            "success"   : True,
            "message"   : f"Transaction created successfully. Transaction id = {transaction_id}",
        }, 200)
    except Exception as e:
        return make_response({
            "success"   : False,
            "message"   : f"Failed to create transaction. Transaction id = {transaction_id}",
            "error"     : str(e)
        }, 500)


@transactions.route("/transaction/<transaction_id>", methods=["GET"])
def get_transaction(transaction_id):
    try:
        transaction = get_transaction_by_id(transaction_id)
        return make_response({
            "success"   : True,
            "data"      : transaction,
        }, 200)
    except Exception as e:
        return make_response({
            "success"   : False,
            "message"   : f"Failed to get transaction. Transaction id = {transaction_id}",
            "error"     : str(e)
        }, 500)


@transactions.route("/types/<type>", methods=["GET"])
def get_transactions_by_type(type):
    try:
        transactions = _get_transaction_by_type(type)
        return make_response({
            "success"   : True,
            "data"      : transactions,
        }, 200)
    except Exception as e:
        return make_response({
            "success"   : False,
            "message"   : f"Failed to get transactions. Transaction type = {type}",
            "error"     : str(e)
        }, 500)


@transactions.route("/sum/<transaction_id>", methods=["GET"])
def get_sum_for_parent_id(transaction_id):
    try:
        final_amount = get_transaction_sum(transaction_id)
        return make_response({
            "success"   : True,
            "data"      : {
                "sum" : final_amount
            },
        }, 200)
    except Exception as e:
        return make_response({
            "success"   : False,
            "message"   : f"Failed to get transactions. Transaction type = {type}",
            "error"     : str(e)
        }, 500)