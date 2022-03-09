from custom_exceptions.id_not_found import IdNotFound
from custom_exceptions.incorrect_info_type import IncorrectInfoType
# from custom_exceptions.duplicate_info import DuplicateInfo
from custom_exceptions.input_length import InputLength
from dal_layer.customer_dal.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer
from service_layer.customer_services.customer_service_interface import CustomerService


class CustomerServiceImp(CustomerService):

    def __init__(self, customer_dobj: CustomerDAOInterface):
        self.customer_dobj = customer_dobj

    def service_new_customer(self, customer: Customer) -> Customer:
        if type(customer.first_name) != str:
            raise IncorrectInfoType("Please put the proper information type in")
        elif type(customer.last_name) != str:
            raise IncorrectInfoType("Please put the proper information type in")
        elif len(customer.first_name) >= 21:
            raise InputLength("Your name is wayyyy to long, <20.")
        elif len(customer.last_name) >= 21:
            raise InputLength("Your name is wayyyy to long, <20.")
        # for current_customer in self.customer_dobj.customers_list:
        #   if current_customer.customer_id == customer.customer_id:
        #      raise DuplicateInfoType("Customer ID already exists.")
        return self.customer_dobj.create_customer(customer)

    def service_get_customer_by_id(self, customer_id):
        try:
            return self.customer_dobj.get_customer_by_id(int(customer_id))
        except ValueError:
            raise IdNotFound("Customer ID not found, please try again.")

    def service_update_customer(self, customer: Customer):
        if type(customer.first_name) != str:
            raise IncorrectInfoType("Please put the proper information type in")
        elif type(customer.last_name) != str:
            raise IncorrectInfoType("Please put the proper information type in")
        elif len(customer.first_name) >= 21:
            raise InputLength("Your name is wayyyy to long, <20.")
        elif len(customer.last_name) >= 21:
            raise InputLength("Your name is wayyyy to long, <20.")
        # for current_customer in self.customer_dobj.customers_list:
        #   if current_customer.customer_info == self.customer_dobj.customer_info:
        #      raise DuplicateInfo("This customer already exists")
        return self.customer_dobj.update_customer_info_by_id(customer)

    def service_delete_customer(self, customer_id):
        if type(customer_id) == int:
            return self.customer_dobj.delete_customer_by_id(customer_id)
        else:
            raise IdNotFound("Customer ID not found, please try again.")
