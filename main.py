import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))