def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)