def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)