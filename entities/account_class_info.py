class Account:
    def __init__(self, account_id: int, account_balance: int, customer_id: int):
        self.account_id = account_id
        self.account_balance = float(account_balance)
        self.customer_id = customer_id
        # self.account_owner = f"Customer Num: {self.customer_id}, Acct Num: {self.account_id}, Acct Bal: {self.account_balance} "

    # def accounts_json_dictionary(self):
    #   return {"Customer ID": self.customer_id,
    #          "Account ID": self.account_id,
    #         "Account Balance": self.account_balance,
    #        "Account Info": self.account_owner}
