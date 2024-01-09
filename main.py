def calculate_area_triangle(b, h):
        return 0.5 * b * h
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))