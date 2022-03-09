from abc import ABC, abstractmethod
from entities.customer_class_info import Customer


class CustomerService(ABC):

    @abstractmethod
    def service_new_customer(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def service_get_customer_by_id(self, customer_id):
        pass

    @abstractmethod
    def service_update_customer(self, customer: Customer):
        pass

    @abstractmethod
    def service_delete_customer(self, customer_id):
        pass
