import math
def calculate_exponential(x):
        return math.exp(x)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))