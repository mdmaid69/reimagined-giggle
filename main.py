import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity