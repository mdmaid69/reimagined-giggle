import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities