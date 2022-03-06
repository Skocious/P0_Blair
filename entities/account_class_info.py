class Account:
    def __init__(self, account_id: int, account_balance: int, customer_id: int):
        self.account_id = account_id
        self.account_balance = account_balance
        self.customer_id = customer_id



"""
Accounts:
    -May not have negative value
    -Must work with numbers
    -Must have unique_id==account_number
"""