import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))