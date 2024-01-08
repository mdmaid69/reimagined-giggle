import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))