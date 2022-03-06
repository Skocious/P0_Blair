from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_imp import AccountDAOImp
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer
from entities.account_class_info import Account

customer_dao = CustomerDAOImp()
account_dao = AccountDAOImp()

"""
Business logic:
    - Customers may not have same unique_id=customer_id
    
    
Will check for correct data for the method and the correct data type

Will check to confirm data exists
Test CRUD
"""

"""
Create Customer Tests
"""


def test_create_customer_success():
    test_customer = Customer(0, "Jane", "Doe")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 0


def test_catch_non_unique_customer_id():
    test_customer = Customer(1, "Steve", "Madden")
    result = customer_dao.create_customer(test_customer)
    assert result.customer_id != 1

"""
Read Customer Tests
"""



def test_get_customer_info_by_id_success():
    result = customer_dao.get_customer_by_id(1)
    assert result.customer_id == 1


def test_get_team_using_non_existent_id():
    try:
        customer_dao.get_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given, please try again!"

"""
Update Customer Tests
"""

def test_update_customer_first_name_by_id_success():
    new_customer_name = Customer(1, "Allen", "Blair")
    result = customer_dao.update_customer_info_by_id(new_customer_name)
    assert result.first_name == "Allen"

def test_update_customer_last_name_by_id_success():
    new_customer_name = Customer(1, "Allen", "Gove")
    result = customer_dao.update_customer_info_by_id(new_customer_name)
    assert result.last_name == "Gove"

#Customer ID will not change

"""
Delete Customer Tests
"""


def test_delete_customer_by_id_success():
    result = customer_dao.delete_customer_by_id(1)
    assert result


def test_delete_customer_id_non_existent_id():
    try:
        customer_dao.delete_customer_by_id(0)
        assert False
    except IdNotFound as e:
        assert str(e) == "No customer matches the id given, please try again!"

