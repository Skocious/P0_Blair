from abc import ABC, abstractmethod
from entities.account_class_info import Account


class AccountService(ABC):

    @abstractmethod
    def service_add_new_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id) -> Account:
        pass

    @abstractmethod
    def service_get_all_accounts_cust_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_update_account(self, account: Account) -> Account:
        pass

    @abstractmethod
    def service_remove_account(self, account: Account) -> bool:
        pass

    @abstractmethod
    def service_withdraw_from_account(self, withdraw_amt: int, account_id) -> Account:
        pass

    @abstractmethod
    def service_deposit_to_account(self, account_id, deposit_amt) -> Account:
        pass

    @abstractmethod
    def service_transfer_between_accounts(self, customer_id, transfer_from_acct, deposit_to_acct, transfer_amt) -> bool:
        pass

