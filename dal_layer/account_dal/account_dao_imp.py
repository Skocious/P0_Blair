# from abc import ABC
# from typing import List
from typing import List

from custom_exceptions.insufficient_funds import InsufficientFunds
from entities.account_class_info import Account
from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_interface import AccountDAOInterface


class AccountDAOImp(AccountDAOInterface):
    account_list = [Account(1, 1000, 1), Account(2, 999, 2)]
    account_id_gen = 3

    # create - will be used to create a new account and add it to database
    def create_account(self, account: Account) -> Account:
        account.account_id = self.account_id_gen
        self.account_id_gen += 1
        AccountDAOImp.account_list.append(account)
        return account

    # read - will be used to retrieve account info via account_id from database
    def get_account_by_id(self, account_id: int) -> Account:
        for account in self.account_list:
            if account.account_id == account_id:
                return account
        raise IdNotFound("Account not found, please try again!")

    def get_all_accounts(self) -> List[Account]:
        account_lis = list(AccountDAOImp.account_list.copy())
        return account_lis

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

    def withdraw_from_acct_by_id(self, withdraw_amt: int, account_id) -> Account:
        if withdraw_amt < 0:
            raise ValueError("Withdraw request can not be a negative number.")
        for account in self.account_list:
            if account.account_id == account_id:
                if withdraw_amt <= account.account_balance:
                    account.account_balance -= withdraw_amt
                print("Withdraw success, your remaining balance is" + str(account.account_balance) + ".")
                return account
            raise IdNotFound("Incorrect account information, please try again.")

    def deposit_to_acct_by_id(self, account_id, deposit_amt) -> Account:
        if deposit_amt < 0:
            raise ValueError("Deposit request can not be a negative number.")
        for account in self.account_list:
            if account_id == account.account_id:
                account.account_balance += deposit_amt
                print("Deposit success, your updated balance is" + str(account.account_balance) + ".")
                return account
        raise IdNotFound("Incorrect account information, please try again.")

    def transfer_between_accts_by_id(self, transfer_from_acct, deposit_to_acct, transfer_amt: float):
        wd_acct = Account(1, 1000, 1)
        dep_acct = Account(1, 1000, 1)
        for account in self.account_list:
            if account.account_id == transfer_from_acct:
                wd_acct = account
            if account.customer_id == deposit_to_acct:
                dep_acct = account
        if wd_acct.account_balance - transfer_amt < 0:
            raise InsufficientFunds("You have insufficient funds for this operation.")
        else:
            wd_acct.account_balance = wd_acct.account_balance - transfer_amt
            dep_acct.account_balance = dep_acct.account_balance + transfer_amt
            return dep_acct.account_balance
