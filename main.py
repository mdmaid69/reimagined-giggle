def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time