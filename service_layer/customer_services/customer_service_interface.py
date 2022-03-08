from abc import ABC, abstractmethod
from entities.customer_class_info import Customer


class CustomerService(ABC):

    @abstractmethod
    def add_new_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def get_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def get_all_customers(self):
        pass

    @abstractmethod
    def update_customer(self, customer: Customer):
        pass

    @abstractmethod
    def remove_customer(self, customer_id):
        pass
