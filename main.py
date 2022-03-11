from flask import Flask, request, jsonify
from custom_exceptions.bad_cust_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_imp import AccountDAOImp
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.account_class_info import Account
from entities.customer_class_info import Customer
from service_layer.account_services.account_service_imp import AccountServiceImp
from service_layer.account_services.account_service_interface import AccountService
from service_layer.customer_services.customer_service_imp import CustomerServiceImp
from api_layer.dict_tool import customer_id_tool
from api_layer.dict_tool import account_id_tool
from api_layer.dict_tool import account_existing_balance

app: Flask = Flask(__name__)  # passing __name__ as an argument lets the object know it should look for its info

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


@app.route("/customer", methods=["POST"])
def create_customer():
    try:
        custd: dict = request.get_json()
        customer = Customer(custd["customerID"], custd["firstName"], custd["lastName"])
        outcome = customer_service.service_new_customer(customer)
        outcome_dict = outcome.cust_json_dictionary()
        outcome_json = jsonify(outcome_dict)
        return outcome_json, 201
    except BadCustomerInfo as e:
        mssg = {"error msg": str(e)}
        return jsonify(mssg), 400
    except IdNotFound as e:
        mssg = {"error msg": str(e)}
        return jsonify(mssg), 400


@app.route("/customer/<customer_id>", methods=["GET"])
def get_customer_by_id(customer_id):
    try:
        outcome: Customer = customer_service.service_get_customer_by_id(customer_id)
        outcome_dict = outcome.cust_json_dictionary()
        outcome_json = jsonify(outcome_dict)
        return outcome_json, 201
    except BadCustomerInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


"""
fdgdfghd
@app.route("/customer/<account_id>", methods=["POST"])
def update_customer_by_id(account_id):
    try:
        new_info: dict = request.get_json()
        cust_id = new_info["customerID"]
        outcome = account_service.service_update_account(cust_id)
        outcome_dict = account_id_tool(outcome)
        outcomejson = jsonify(outcome_dict)
        return outcomejson, 201
    except BadCustomerInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
"""


@app.route("/account/<account_id>", methods=["GET"])
def get_account_info(account_id):
    try:
        outcome: Account = account_service.service_get_account_by_id(account_id)
        outcome_dict = outcome.accounts_json_dictionary()
        outcomejson = jsonify(outcome_dict)
        return outcomejson
    except BadCustomerInfo as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400
    except IdNotFound as e:
        message = {
            "message": str(e)
        }
        return jsonify(message), 400


app.run()
