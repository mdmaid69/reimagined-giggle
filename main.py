def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import os
def get_environment_variable(var):
        return os.getenv(var)