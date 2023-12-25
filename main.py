def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time