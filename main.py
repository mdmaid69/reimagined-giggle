def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))