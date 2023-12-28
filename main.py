import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))