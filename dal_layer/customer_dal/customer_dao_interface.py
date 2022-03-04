# CRUD operations here
from abc import ABC, abstractmethod
from entities.customer_class_info import Customer


class CustomerDAOInterface(ABC):

    # create - will be used to add new customer data to database
    @abstractmethod
    def create_customer(self, customer: Customer) -> Customer:
        pass

    # read - will be used to retrieve customer data via customer_id from database
    @abstractmethod
    def get_customer_by_id(self, customer_id: int) -> Customer:
        pass

    # update - will be used to update customer information in database via customer_id
    @abstractmethod
    def update_customer_info_by_id(self, customer: Customer) -> Customer:
        pass

    # delete - will be used to delete customer account info from database - check for != 0 balance
    @abstractmethod
    def delete_customer_by_id(self, customer_id: int) -> bool:
        pass
