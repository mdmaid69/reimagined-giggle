import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding