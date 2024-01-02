def calculate_area(radius):
        return 3.14 * radius * radius
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))