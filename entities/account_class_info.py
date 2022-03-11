class Account:
    def __init__(self, account_id: int, account_balance: int, customer_id: int):
        self.account_id = account_id
        self.account_balance = account_balance
        self.customer_id = customer_id

    def __str__(self):
        self.account_owner = f"CustID: {self.customer_id}, AcctID: {self.account_id}, Acct Bal: {self.account_balance} "

    def accounts_json_dictionary(self):
        return {
                "accountID": self.account_id,
                "accountBalance": self.account_balance,
                "customerID": self.customer_id
                }
