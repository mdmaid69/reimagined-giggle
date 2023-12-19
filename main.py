def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)