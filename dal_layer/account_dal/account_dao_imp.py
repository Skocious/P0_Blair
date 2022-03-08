# from abc import ABC
# from typing import List

from entities.account_class_info import Account
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_interface import AccountDAOInterface


class AccountDAOImp(AccountDAOInterface):
    account_list = [Account(1, 0, 1)]
    account_id_gen = 2
    # account_dict = {}

    # create - will be used to create a new account and add it to database
    def create_account(self, account: Account) -> Account:
        account.account_id = self.account_id_gen
        self.account_id_gen += 1
        self.account_list.append(account)
        return account

    # read - will be used to retrieve account info via account_id from database
    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
        raise IdNotFound("Account not found, please try again!")

    # def get_all_accounts(self) -> List[Account]:
    #    account_list = list(AccountDAOImp.account_dict.values())
    #    return account_list

    # update - will be used to update account information in database via account_id
    def update_account_info_by_id(self, account: Account) -> Account:
        for old_account_info in self.account_list:
            if old_account_info.account_id == account.account_id:
                old_account_info = account
                return old_account_info
        raise IdNotFound("Account not found, please try again!")

    # delete - will be used to delete account from database
    def delete_account_by_id(self, account_id: int) -> bool:
        for account in self.account_list:
            if account.account_id == account_id:
                self.account_list.remove(account)
                return True
        raise IdNotFound("Account not found, please try again!")
