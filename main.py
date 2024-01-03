import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities