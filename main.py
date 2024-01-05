def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))