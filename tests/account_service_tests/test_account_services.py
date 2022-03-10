from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_imp import AccountDAOImp
from dal_layer.account_dal.account_dao_interface import AccountDAOInterface
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from dal_layer.customer_dal.customer_dao_interface import CustomerDAOInterface
from entities.account_class_info import Account
from service_layer.account_services.account_service_imp import AccountServiceImp
from entities.customer_class_info import Customer
from service_layer.account_services.account_service_interface import AccountService

account_daoj: AccountDAOInterface = AccountDAOImp()
account_sevj = AccountServiceImp(account_daoj)
customer_daoj: CustomerDAOInterface = CustomerDAOImp()


def test_get_all_cust_acct():

    account = account_sevj.service_get_all_accounts_cust_id(1)
    assert len(account) >= 1



def test_get_cust_acct_by_cust_id():
    cust1 = Customer(0, "Jane", "Doe")
    cust2 = Customer(0, "Janice", "Eod")
    customer_daoj.create_customer(cust1)
    customer_daoj.create_customer(cust2)
    cust1 = customer_daoj.get_customer_by_id(1)
    cust2 = customer_daoj.get_customer_by_id(2)
    print()
    print(cust1.customer_id)
    print(cust2.customer_id)
    outcome: Account = account_sevj.service_get_account_by_id(1)
    assert outcome.customer_id == 1


def test_update_account_by_id():
    try:
        acct = account_daoj.get_account_by_id(1)
        account_sevj.service_update_account(acct)
        outcome = account_daoj.get_account_by_id(1)
        assert outcome.account_owner == acct.account_owner
    except IdNotFound:
        assert IdNotFound("Account ID not found, please try again.")


def test_remove_account_by_id():
    try:
        acct = account_daoj.delete_account_by_id(2)
        account_sevj.service_remove_account(acct)
        assert True
    except IdNotFound:
        assert IdNotFound("Account ID not found, please try again.")


def test_withdraw_from_account():
    try:
        wd = 100
        acct = account_sevj.service_get_account_by_id(1)
        acct.account_balance -= wd
        account_sevj.service_withdraw_from_account(1, 1)
        acct2 = account_sevj.service_get_account_by_id(1)
        assert acct.account_balance == acct2.account_balance
    except ValueError:
        assert ValueError("Insufficient funds.")
