import math
def calculate_hyperbolic_tangent(x):
        return math.tanh(x)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))