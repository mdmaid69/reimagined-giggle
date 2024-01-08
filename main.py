def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_circumference_circle(r):
        return 2 * 3.14 * r