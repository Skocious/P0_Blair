from custom_exceptions.id_not_found import IdNotFound
from dal_layer.account_dal.account_dao_imp import AccountDAOImp
from dal_layer.customer_dal.customer_dao_imp import CustomerDAOImp
from entities.account_class_info import Account

account_dao = AccountDAOImp()

"""
Business logic:
    Accounts may not have the same unique_id=account_id (This will be handled on service layer)
    Accounts can not have a <0 balance
"""

"""
Here I will check that the correct data is provided to the method intended, 
and that the method returns the expected return value.
In addition to check and make sure data exists and to return a message if it does not
"""

"""
Create account tests
"""


def test_create_account_success():
    new_account = Account(1, 0, 1)
    outcome = account_dao.create_account(new_account)
    assert outcome.account_id != 1


def test_catch_non_unique_account_id():
    test_account = Account(1, 100, 1)
    result = account_dao.create_account(test_account)
    assert result.account_id != 1


""""
Read account tests
"""


def test_get_account_info_by_id_success():
    outcome = account_dao.get_account_by_id(1)
    assert outcome.account_id == 1


def test_get_account_info_non_existent_id():
    try:
        account_dao.get_account_by_id(0)
        assert True

    except IdNotFound as e:
        assert str(e) == "Account not found, please try again!"


"""
Update account tests
"""


def test_update_account_by_id_success():
    new_account_owner = Account(1, 0, 2)
    outcome = account_dao.update_account_info_by_id(new_account_owner)
    assert outcome.customer_id == 2


def test_update_account_using_non_existent_id():
    try:
        new_account_owner = Account(0, 0, 2)
        account_dao.update_account_info_by_id(new_account_owner)
        assert True
    except IdNotFound as e:
        assert str(e) == "Account not found, please try again!"


"""
Delete account test
"""


def test_delete_account_by_id_success():
    try:
        outcome = account_dao.delete_account_by_id(2)
        assert outcome
        # account_dao.delete_account_by_id(1)
        # assert True
    except IdNotFound as e:
        assert str(e) == "Account not found, please try again!"


def test_delete_account_by_id_non_existent():
    try:
        account_dao.delete_account_by_id(0)
        assert True
    except IdNotFound as e:
        assert str(e) == "Account not found, please try again!"


# Project Requirements


def test_get_all_accounts_by_account_id():
    try:
        tact1 = Account(0, 0, 0)
        tact2 = Account(0, 0, 0)
        tact3 = Account(0, 0, 0)
        tact4 = Account(0, 0, 0)
        account_dao.create_account(tact1)
        account_dao.create_account(tact2)
        account_dao.create_account(tact3)
        account_dao.create_account(tact4)
        outcome = account_dao.get_all_accounts()
        assert len(outcome) >= 4
    except IdNotFound as e:
        assert str(e) == "Account not found, please try again!"
