import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets