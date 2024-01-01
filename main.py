def calculate_simple_interest(principal, rate, time):
        return principal * rate * time
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)