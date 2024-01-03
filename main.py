import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps