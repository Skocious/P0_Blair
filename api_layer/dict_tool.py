def customer_id_tool(customer_id):
    tool_dict = {"Client_ID": customer_id}
    return tool_dict


def account_id_tool(account_id):
    tool_dict = {"Account_ID": account_id}
    return tool_dict


def account_existing_balance(account_id, account_balance):
    tool_dict = {"Account_ID": account_id, "Current_Account_Balance": account_balance}
    return tool_dict
