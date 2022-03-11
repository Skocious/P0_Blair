from custom_exceptions.id_not_found import IdNotFound
from entities.account_class_info import Account
from service_layer.account_services.account_service_interface import AccountService
from dal_layer.account_dal.account_dao_interface import AccountDAOInterface


class AccountServiceImp(AccountService):

    def __init__(self, account_dao: AccountDAOInterface):
        self.account_dao = account_dao

    def service_add_new_account(self, account: Account):
        return self.account_dao.create_account(account)

    def service_get_account_by_id(self, account_id: int):
        if type(account_id) == int:
            return self.account_dao.get_account_by_id(account_id)
        else:
            raise IdNotFound("Customer ID not found, please try again.")

    def service_get_all_accounts_cust_id(self, account: Account):
        if type(account) == int:
            accounts = self.account_dao.get_all_accounts()
            cust_accts = []
            for a in accounts:
                if a.customer_id == account:
                    cust_accts.append(a)
            return cust_accts
        else:
            raise IdNotFound("Customer ID not found, please try again.")

    def service_update_account(self, account: Account):
        if type(self.account_dao.update_account_info_by_id(account)) == int:
            return self.account_dao.update_account_info_by_id(account)
        else:
            raise IdNotFound("Account ID not found, please try again.")

    def service_remove_account(self, account_id: int):
        if type(account_id) == int:
            return self.account_dao.delete_account_by_id(account_id)
        else:
            raise IdNotFound("Account ID not found, please try again.")

    def service_withdraw_from_account(self, withdraw_amt: int, account_id):
        if withdraw_amt < 0:
            raise ValueError("Insufficient funds.")
        acct = self.account_dao.get_account_by_id(account_id)
        if withdraw_amt > float(acct.account_balance):
            raise ValueError("Insufficient funds.")
        new_bal = float(acct.account_balance) - withdraw_amt
        acct.account_balance = new_bal
        return self.account_dao.update_account_info_by_id(acct)

    def service_deposit_to_account(self, deposit_amt, account_id) -> Account:
        if deposit_amt < 0:
            raise ValueError("Deposit request can not be a negative number.")
        acct = self.service_get_account_by_id(account_id)
        new_bal = float(acct.account_balance) + deposit_amt
        acct.account_balance = new_bal
        return self.service_update_account(account_id)

    def service_transfer_between_accounts(self, customer_id, transfer_from_acct, deposit_to_acct, transfer_amt):
        if transfer_amt < 0:
            raise ValueError("Invalid amount, can not transfer less than $0")
        transfer_from_acct = self.account_dao.get_account_by_id(transfer_from_acct)
        transfer1 = transfer_from_acct.account_balance - transfer_amt
        transfer_from_acct.account_balance = transfer1
        return self.account_dao.update_account_info_by_id(deposit_to_acct)


