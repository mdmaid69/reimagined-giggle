def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)