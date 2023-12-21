def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time