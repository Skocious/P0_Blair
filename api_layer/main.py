from flask import Flask, request, jsonify

from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer

app: Flask = Flask(__name__)  # passing __name__ as an argument lets the object know it should look fir its info
customer_dao = CustomerDAOImp()
customer_Service = CustomerServiceImp(customer_dao)


@app.route("/customer", methods=["GET"])
def create_customer():
    try:
        custd: dict = request.get_json()
        customer = Customer(custd["customer_id"], custd["first_name"], custd["last_name"])
        outcome = customer_Service.service_create_customer(customer)
        outcome_dict = outcome.dict_conv()
        outcome_json = jsonify(outcome_dict)
        return outcome_json, 201
    except BadCustInfo as e:
        emsg = {"emsg": str(e)}
        return jsonify(mssg), 400
    except IdNotFound as e:
        emsg = {"emsg": str(e)}
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
