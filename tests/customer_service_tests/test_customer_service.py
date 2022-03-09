from custom_exceptions.incorrect_info_type import IncorrectInfoType
from custom_exceptions.input_length import InputLength
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer
from service_layer.customer_services.customer_service_imp import CustomerServiceImp

customer_daoj = CustomerDAOImp()
customer_serj = CustomerServiceImp(customer_daoj)

# Test for ID Len
len_first_name_create = Customer(1, "William", "Blair")
len_last_name_create = Customer(1, "William", "Blair")
len_first_name_update = Customer(1, "William", "Blair")
len_last_name_update = Customer(1, "William", "Blair")

# Test for Type
type_first_name_create = Customer(1, 1, "Blair")
type_last_name_create = Customer(1, "William", 1)
type_first_name_update = Customer(1, 1, "Blair")
type_last_name_update = Customer(1, "William", 1)

# Test for Unique ID ?????????????????????????????
unique_cust_id_1 = Customer(1, "William", "Blair")
unique_cust_id_2 = Customer(2, "William", "Blair")


# I can have duplicate names so how do I check for dup id creation?

def test_ck_type_fn_c():
    try:
        customer_serj.service_new_customer(type_first_name_create)
        assert False
    except IncorrectInfoType as e:
        assert str(e) == "Please put the proper information type in"


def test_ck_type_ln_c():
    try:
        customer_serj.service_new_customer(type_last_name_create)
        assert False
    except IncorrectInfoType as e:
        assert str(e) == "Please put the proper information type in"


def test_ck_type_fn_u():
    try:
        customer_serj.service_update_customer(type_first_name_update)
        assert False
    except IncorrectInfoType as e:
        assert str(e) == "Please put the proper information type in"


def test_ck_type_ln_u():
    try:
        customer_serj.service_update_customer(type_last_name_update)
        assert False
    except IncorrectInfoType as e:
        assert str(e) == "Please put the proper information type in"


def test_ck_len_fn_c():
    try:
        customer_serj.service_new_customer(len_first_name_create)
        assert True
    except InputLength as e:
        assert str(e) == "Your name is wayyyy to long, <20."


def test_ck_len_ln_c():
    try:
        customer_serj.service_new_customer(len_last_name_create)
        assert True
    except InputLength as e:
        assert str(e) == "Your name is wayyyy to long, <20."


def test_ck_len_fn_u():
    try:
        customer_serj.service_new_customer(len_first_name_update)
        assert True
    except InputLength as e:
        assert str(e) == "Your name is wayyyy to long, <20."


def test_ck_len_ln_u():
    try:
        customer_serj.service_new_customer(len_last_name_update)
        assert True
    except InputLength as e:
        assert str(e) == "Your name is wayyyy to long, <20."


