from abc import ABC, abstractmethod
from typing import List

from entities.account_class_info import Account


# from typing import List


class AccountDAOInterface(ABC):

    # create - will be used to create a new account and add it to database
    @abstractmethod
    def create_account(self, account: Account) -> Account:
        pass

    # read - will be used to retrieve account info via account_id from database
    @abstractmethod
    def get_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_all_accounts(self) -> List[Account]:
        pass

    # update - will be used to update account information in database via account_id
    @abstractmethod
    def update_account_info_by_id(self, account: Account) -> Account:
        pass

    # delete - will be used to delete account from database - check for != 0 balance
    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass

    @abstractmethod
    def withdraw_from_acct_by_id(self, withdraw_amt: int, account_id) -> Account:
        pass

    @abstractmethod
    def deposit_to_acct_by_id(self, account_id, deposit_amt) -> Account:
        pass

    @abstractmethod
    def transfer_between_accts_by_id(self, transfer_from_acct, deposit_to_acct, transfer_amt) -> bool:
        pass

