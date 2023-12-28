import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets