from abc import ABC, abstractmethod
from entities.account_class_info import Account
from entities.customer_class_info import


class CustomerService(ABC):

    @abstractmethod
    def add_new_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def get_account_by_id(self, account_id): ->

    Account:
    pass


@abstractmethod
def get_all_accounts_by_cid(self, account_id, customer_id):
    pass


@abstractmethod
def update_account(self, account: Account) -> Account:
    pass


@abstractmethod
def remove_account(self, account_id): ->


Account:
pass
