class Account:
    def __init__(self, account_number: int, account_balance: int, customer_id: int):
        self.account_number = account_number
        self.account_balance = account_balance
        self.customer_id = customer_id



"""
Accounts:
    -May not have negative value
    -Must work with numbers
    -Must have unique_id==account_number
"""