import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))