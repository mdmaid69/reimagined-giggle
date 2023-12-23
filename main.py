import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities