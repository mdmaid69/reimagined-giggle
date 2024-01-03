def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time