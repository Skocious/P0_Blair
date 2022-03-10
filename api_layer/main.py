from flask import Flask, request, jsonify
from custom_exceptions.bad_cust_info import BadCustomerInfo
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_imp import AccountDAOImp
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer
from service_layer.account_services.account_service_imp import AccountServiceImp
from service_layer.account_services.account_service_interface import AccountService
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)  # passing __name__ as an argument lets the object know it should look fir its info

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)
account_dao = AccountDAOImp()
account_service = AccountServiceImp(account_dao)


@app.route("/customer", methods=["POST"])
def create_customer():
    try:
        custd: dict = request.get_json()
        customer = Customer(custd["customer_id"], custd["first_name"], custd["last_name"])
        outcome = customer_service.service_new_customer(customer)
        outcome_dict = outcome.cust_json_dictionary()
        outcome_json = jsonify(outcome_dict)
        return outcome_json, 201
    except BadCustomerInfo as e:
        mssg = {"emsg": str(e)}
        return jsonify(mssg), 400
    except IdNotFound as e:
        mssg = {"emsg": str(e)}
        return jsonify(mssg), 400


"""
@app.route("/personal/<name>", methods=["GET"])
def personal_greeting(name: str):
    return f"Hello {name}!"

@app.route("/ass/<num_one>/<num_two>", methods=["GET"])
def addition_function(num_one: str, num_two: str):
    result = int(num_one) + int(num_two)
    return str(result)

@app.route("/list/<index>", methods=["GET"])
def get_phrase_from_list(index: str):
    global my_list
    return my_list[int(index)]

@app.route("/list", methods=["GET"])
def get_all_phrases_from_list():
    global my_list
    my_json_list = jsonify(my_list)
    return my_json_list, 202


@app.route("/list", methods=["POST"])
def add_phrase_to_list():
    request_content = request.get_json() #this method turns our JSON into a python dictionary
    global my_list
    my_list.append(request_content["key"])
    return "Phrase added"

@app.route("/json", methods=["GET"])
def return_a_json():
    cuatomer_id = 1
    first_name = "Ted"
    last_name = "Teddington"
"""
"""
json uses java naming conventions, use camelCase


    customer_as_dictionary = {
        "customerId": cuatomer_id,
        "firstName": first_name,
        "lastName": last_name
    }

    customer_as_json = jsonify(customer_as_dictionary)
    return customer_as_json, 202


@app.route("/query", methods=["GET"])
def get_filtered_phrases():
    min_index = request.args["min"]
    max_index = request.args["max"]
    global my_list
    return_list = []
    for index in range(0, len(my_list), 1):
        if index >= int(min_index) and index <= int(max_index):
            return_list.append(my_list[index])
    return_list_as_json = jsonify(return_list)
    return return_list_as_json, 200
"""

# jsonify turns your result into a JSON list (JAVA)

# fix index outta bounds by adding - 1 or make sure you are starting at 0


app.run()
