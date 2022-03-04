from custom_exceptions.id_not_found import IdNotFound
from dal_layer.customer_dal.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerDAOImp(CustomerDAOInterface, ABC):

    def __init__(self):
        customer_id_catch = Customer(1, "William", "Blair")
        self.customers_list = []
        self.customer_id_generator = 2
        self.customers_list.append(customer_id_catch)

    def create_customer(self, customer: Customer) -> Customer:
        customer.customer_id = self.customer_id_generator
        self.customer_id_generator += 1
        self.customers_list.append(customer)

    def get_customer_by_id(self, customer_id: int) -> Customer:
        for customer in self.customers_list:
            if customer.customer_id == customer_id:
                return customer
        raise IdNotFound("No customer matches the id given, please try again!")

    def update_customer_info_by_id(self, customer: Customer) -> Customer:
        for old_cus_info in self.customers_list:
            if customer.customer_id == old_cus_info.customer_id:
                old_cus_info = customer
                return old_cus_info
        raise IdNotFound("No customer matches the id given, please try again!")

    def delete_customer_by_id(self, customer_id: int) -> bool:
        for customer in self.customers_list:
            if customer.customer_id == customer_id:
                self.customers_list.remove(customer)
                return True
        raise IdNotFound("No customer matches the id given, please try again!")
