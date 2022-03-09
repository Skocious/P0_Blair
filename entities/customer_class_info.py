class Customer:

    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        self.customer_info = f"Customer Info: {self.first_name}, {self.last_name}, Customer ID#:{self.customer_id}"

    def cust_json_dictionary(self):
        return {"Customer Info": self.customer_info,
                "FirstName": self.first_name,
                "LastName": self.last_name,
                "CustomerID": self.customer_id}
